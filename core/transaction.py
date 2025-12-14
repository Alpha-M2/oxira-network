import json
from utils.hashing import hash_json


class Transaction:
    def __init__(self, sender, recipient, value, nonce, gas=21000):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.nonce = nonce
        self.gas = gas
        self.signature = None

    def hash(self):
        return hash_json(self.__dict__)

    def sign(self, wallet):
        self.signature = wallet.sign(self.hash().encode())
