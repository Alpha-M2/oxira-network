from compiler.solidity_compiler import compile_contract
from evm.mini_evm import MiniEVM
from evm.deploy import deploy_contract, execute_contract
from core.state import State


def test_compile_contract_bytecode_shape():
    bc = compile_contract("x = x + 1")
    assert bc[:6] == ["LOAD", "x", "PUSH", 1, "ADD", "STORE"]
    # ensure STORE has the key operand after it
    assert bc[6] == "x"
    assert bc[-1] == "STOP"


def test_mini_evm_increment_storage():
    code = compile_contract("x = x + 1")
    storage = {"x": 0}
    evm = MiniEVM(code, storage, gas=100)
    evm.run()
    assert storage["x"] == 1


def test_execute_contract_updates_state_storage():
    s = State()
    code = compile_contract("x = x + 1")
    addr = deploy_contract(s, code)
    # ensure account storage exists
    acct = s.get_account(addr)
    acct.storage["x"] = 0

    # execute the contract and confirm storage updated
    execute_contract(s, addr, gas=100)
    assert s.get_account(addr).storage.get("x", None) == 1
