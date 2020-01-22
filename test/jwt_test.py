import unittest
import sys,os
sys.path.append(os.path.abspath("./"))
from pkg.auth import JWT

class TestJWT(unittest.TestCase):

    def test_JWT(self):
        secret = JWT().encode({"name": "Bob"})
        self.assertEqual(
            JWT().decode(secret).get("name",""), 
            "Bob"
        )

if __name__ == '__main__':
    unittest.main()