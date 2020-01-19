from flask import Blueprint

login = Blueprint('login', __name__)

@login.route('/api/login', methods=['GET', 'POST'])
def index():
    return 'Hello World!'