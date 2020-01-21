
class User:
    def __init__(self, userDict:dict):
        self.userName = userDict.get('username','')
        self.passWord = userDict.get('password','')