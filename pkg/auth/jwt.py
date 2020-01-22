import jwt

def readKey(path: str) ->bytes:
    with open(path) as f:
        return f.read()

class JWT:
    def __init__(self):
        self._private_key = readKey("./resources/secret/rsa_private_key.pem")
        self._public_key  = readKey("./resources/secret/rsa_public_key.pem")
        self.InvalidSignatureError = jwt.exceptions.InvalidSignatureError

    def encode(self, payload: dict) -> bytes:
        return jwt.encode(payload, self._private_key, algorithm='RS256')

    def decode(self, encoded: bytes) -> dict:
        return jwt.decode(encoded, self._public_key, algorithms='RS256')