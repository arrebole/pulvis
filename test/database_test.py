import unittest
import sys,os
sys.path.append(os.path.abspath("./"))
from pkg.database import UserCtl
from pkg.types import User

class TestDatabase(unittest.TestCase):

    def test_UserCtl(self):
        db = UserCtl()
        db.addUser(User({'userName': "test",'passWord': "123"}))
        self.assertEqual(
            db.exist(User({'userName': "test",'passWord': "123"})), 
            (True, True)
        )

if __name__ == '__main__':
    unittest.main()