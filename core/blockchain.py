import json
import hashlib
from core.block import Block


class Blockchain:
    def __init__(self, state):
        self.chain = []
        self.state = state
        self.pending = []
        self.create_genesis()

    def create_genesis(self):
        self.chain.append(Block(0, "0" * 64, [], None, 0))

    def add_transaction(self, tx):
        self.pending.append(tx)

    def mine(self):
        prev = self.chain[-1]
        snapshot = json.dumps(
            {k: v.__dict__ for k, v in self.state.accounts.items()}, sort_keys=True
        ).encode()
        state_root = hashlib.sha256(snapshot).hexdigest()
        nonce = 0
        while (
            not hashlib.sha256(f"{prev.hash()}{nonce}".encode())
            .hexdigest()
            .startswith("0000")
        ):
            nonce += 1
        block = Block(len(self.chain), prev.hash(), self.pending, state_root, nonce)
        self.chain.append(block)
        self.pending = []
        return block
