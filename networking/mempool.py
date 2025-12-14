class Mempool:
    def __init__(self):
        self.pool = []

    def add(self, tx):
        self.pool.append(tx)

    def select(self):
        return sorted(self.pool, key=lambda t: t.gas, reverse=True)
