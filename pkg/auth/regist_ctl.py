from flask import Blueprint, request
from pkg.database import UserCtl
from pkg.types import User

regist = Blueprint('regist', __name__)

@regist.route('/api/regist', methods=['GET', 'POST'])
def index():
    if UserCtl().addUser(User(request.json)):
        return '创建用户成功!'
    return "创建用户失败"