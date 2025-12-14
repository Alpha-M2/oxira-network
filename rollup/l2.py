import hashlib


class Rollup:
    def __init__(self):
        self.batch = []

    def submit(self, tx):
        self.batch.append(tx)

    def commit(self):
        return hashlib.sha256(str(self.batch).encode()).hexdigest()


def verify_rollup(batch_hash, batch):
    return hashlib.sha256(str(batch).encode()).hexdigest() == batch_hash
