from flask import Blueprint, request, jsonify
from pkg.database import UserCtl
from pkg.types import User

regist = Blueprint('regist', __name__)

def resp(code: int, msg: str):
    return jsonify({ "code": code, "message": msg, "data": None })


@regist.route('/api/regist', methods=['GET', 'POST'])
def index():
    if UserCtl().addUser(User(request.json)):
        return resp(0, '创建用户成功!')
    return resp(-1, "创建用户失败")