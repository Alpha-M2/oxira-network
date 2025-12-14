from evm.deploy import execute_contract


class AIAgent:
    def __init__(self, wallet):
        self.wallet = wallet

    def act(self, state, contract_address):
        execute_contract(state, contract_address, gas=1000)
