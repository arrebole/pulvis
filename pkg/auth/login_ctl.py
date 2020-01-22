from flask import Blueprint, request, jsonify
from pkg.database import UserCtl
from pkg.types import User
from .jwt import JWT
import datetime

login = Blueprint('login', __name__)

def success(token: str):
    return jsonify({ "code": 0, "message": "success", "data": { "token": token }})

def fail(msg: str):
    return jsonify({ "code": -1, "message": msg,  "data": None })


@login.route('/api/login', methods=['GET', 'POST'])
def index():
    user = User(request.json)
    
    if UserCtl().exist(user) == (True, True):
        token = str(JWT().encode({
            "username": user.userName, 
            "exp":      datetime.datetime.utcnow() + datetime.timedelta(days=3)
        }), encoding="utf-8")
        return success(token)

    return fail("用户名或密码错误")