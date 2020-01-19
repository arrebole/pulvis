from flask import Flask

def setup(app: Flask):
    from .regist_ctl import regist
    from .login_ctl import login
    
    app.register_blueprint(login)
    app.register_blueprint(regist)
    return app