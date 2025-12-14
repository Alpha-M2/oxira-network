class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.nonce = 0
        self.storage = {}


class State:
    def __init__(self):
        self.accounts = {}

    def get_account(self, address):
        if address not in self.accounts:
            self.accounts[address] = Account()
        return self.accounts[address]
