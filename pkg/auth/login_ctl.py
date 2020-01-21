import json
from flask import Blueprint, request
from pkg.database import UserCtl

login = Blueprint('login', __name__)

class User:
    def __init__(self, jsonObj:dict):
        self.userName = jsonObj.get('username','')
        self.passWord = jsonObj.get('password','')

@login.route('/api/login', methods=['GET', 'POST'])
def index():
    if UserCtl().exist(User(request.json)) == (True, True):
        return "登录成功"
    return '用户名或密码错误'