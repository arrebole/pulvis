from flask import Flask
from .jwt import JWT

def setup(app: Flask):
    from .regist_ctl import regist
    from .login_ctl import login
    from .verify_ctl import verify
    
    app.register_blueprint(login)
    app.register_blueprint(regist)
    app.register_blueprint(verify)
    return app

all = ["setup", "JWT"]