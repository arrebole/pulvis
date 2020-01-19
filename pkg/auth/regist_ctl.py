from flask import Blueprint

regist = Blueprint('regist', __name__)

@regist.route('/api/regist', methods=['GET', 'POST'])
def index():
    return 'Hello World!'