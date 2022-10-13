from flask import Blueprint, request
import sys
import jwt
from flask_cors import cross_origin
from db import db
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

local_array = {}

@auth_api.route("/register", methods=["POST"])
@cross_origin(supports_credentials=True)
def register_user():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        local_array[username] = password
        return {'status': 'success'}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500


@auth_api.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login_user():
    try:
        username = request.args.get('username')
        hashedPassword = request.args.get('hashedPassword')
        if local_array[username] != hashedPassword:
            return {"status": "failed", "err": "username and password does not match"}
        else:
            key = 'secret'
            encoded = jwt.encode(local_array, key)
            return {"status": "success", "data": encoded}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500