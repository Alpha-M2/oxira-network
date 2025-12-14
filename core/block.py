import json
from time import time
from utils.hashing import sha256


class Block:
    def __init__(self, index, prev_hash, txs, state_root, nonce):
        self.index = index
        self.prev_hash = prev_hash
        self.transactions = txs
        self.state_root = state_root
        self.nonce = nonce
        self.timestamp = time()

    def hash(self):
        header = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(header)
