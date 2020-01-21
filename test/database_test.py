import unittest

import sys,os
sys.path.append(os.path.abspath("./pkg"))
from database import UserCtl

class User:
    def __init__(self, u, p):
        self.userName = u
        self.passWord = p

class TestDatabase(unittest.TestCase):

    def test_UserCtl(self):
        db = UserCtl()
        db.addUser(User("test","123"))
        self.assertEqual(db.exist(User("test","123")), (True, True))


if __name__ == '__main__':
    unittest.main()