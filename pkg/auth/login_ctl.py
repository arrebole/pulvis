from flask import Blueprint, request
from pkg.database import UserCtl
from pkg.types import User

login = Blueprint('login', __name__)

@login.route('/api/login', methods=['GET', 'POST'])
def index():
    if UserCtl().exist(User(request.json)) == (True, True):
        return "登录成功"
    return '用户名或密码错误'