from flask import Blueprint, request, jsonify
from .jwt import JWT

verify = Blueprint('verify', __name__)

def resp(code: int, msg: str):
    return jsonify({ "code": code, "message": msg, "data": None })

def isPass(token) -> bool:
    try:
        JWT().decode(token)
    except BaseException:
        return False
    return True

@verify.route('/api/verify', methods=['GET', 'POST'])
def index():
    # 1、从cookie中获取token
    token = request.cookies.get('token') 

    # 2、如果cookie中没有，则在url中获取
    if token == None:
        token = request.args.get('token')

    # 2、如果url中没有，则在post中获取
    if token == None:
        token = request.json.get('token')

    if not isPass(token):
        return resp(-1, "fail")
    
    return resp(0, "pass")