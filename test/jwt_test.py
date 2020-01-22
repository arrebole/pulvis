import unittest
import sys,os
sys.path.append(os.path.abspath("./"))
from pkg.auth import JWT

class TestJWT(unittest.TestCase):

    def test_JWT(self):
        jwt = JWT()
        secret = jwt.encode({"name": "Bob"})
        
        self.assertEqual(
            jwt.decode(secret).get("name",""), 
            "Bob"
        )
        
        try:
            jwt.decode(secret+ b'a')
        except jwt.InvalidSignatureError:
            pass
        else:
            self.fail()

if __name__ == '__main__':
    unittest.main()