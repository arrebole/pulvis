from flask import Blueprint, request, jsonify
from pkg.database import UserCtl
from pkg.types import User
from .jwt import JWT

login = Blueprint('login', __name__)

@login.route('/api/login', methods=['GET', 'POST'])
def index():
    user = User(request.json)
    
    if UserCtl().exist(user) == (True, True):
        token = str(JWT().encode({"username": user.userName}), encoding="utf-8")
        return jsonify({ "token":  token })

    return '用户名或密码错误'