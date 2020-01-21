import sqlite3, os
from pkg.types import User

class UserCtl:
    def __init__(self):
        self._conn: sqlite3.Connection = sqlite3.connect(os.path.abspath('./resources/database/database.db'))
    
    # 添加新用户
    def addUser(self, user: User)-> bool:
        if self.exist(user)[0]:
            return False
        
        self._conn.cursor().execute(
            f"INSERT INTO users (username, password) VALUES('{user.userName}', '{user.passWord}');"
        )
        self._conn.commit()
        return True


    # exist 验证用(户名是否存在，密码是否合法)
    def exist(self, user: User)->tuple():
        data = self._conn.cursor().execute(
            f"SELECT * FROM users WHERE username='{user.userName}' LIMIT 1"
        ).fetchall()

        # 用户名不存在
        if len(data) == 0:
            return (False, False)
        
        # 用户名存在 但是密码不正确
        if data[0][2] != user.passWord:
            return (True, False)
        
        # 用户名存在 并且密码正确
        return (True, True)
        