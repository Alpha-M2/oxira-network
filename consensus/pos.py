class Validator:
    def __init__(self, address, stake):
        self.address = address
        self.stake = stake


class Casper:
    def __init__(self):
        self.votes = {}

    def vote(self, validator, block_hash):
        self.votes.setdefault(block_hash, 0)
        self.votes[block_hash] += validator.stake

    def finalized(self, block_hash, total_stake):
        return self.votes.get(block_hash, 0) > (2 / 3) * total_stake
