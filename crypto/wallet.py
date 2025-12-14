import hashlib
from ecdsa import SigningKey, SECP256k1


class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def address(self):
        return hashlib.sha256(self.public_key.to_string()).hexdigest()[:40]

    def sign(self, message: bytes):
        return self.private_key.sign(message)
