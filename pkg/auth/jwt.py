import jwt

def readKey(path: str) ->bytes:
    with open(path) as f:
        return f.read()

defaultPrivateKey = readKey("./resources/secret/rsa_private_key.pem")
defaultPublicKey = readKey("./resources/secret/rsa_public_key.pem")

class JWT:
    def __init__(self):
        self._private_key, self._public_key = defaultPrivateKey, defaultPublicKey 

    def encode(self, payload: dict) -> bytes:
        return jwt.encode(payload, self._private_key, algorithm='RS256')

    def decode(self, encoded: bytes) -> dict:
        return jwt.decode(encoded, self._public_key, algorithms='RS256')