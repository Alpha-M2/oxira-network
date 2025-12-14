import hashlib
from evm.mini_evm import MiniEVM


def deploy_contract(state, bytecode):
    address = hashlib.sha256(str(bytecode).encode()).hexdigest()[:40]
    account = state.get_account(address)
    account.code = bytecode
    return address


def execute_contract(state, address, gas):
    account = state.get_account(address)
    evm = MiniEVM(account.code, account.storage, gas)
    evm.run()
