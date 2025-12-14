from crypto.wallet import Wallet
from core.state import State
from core.blockchain import Blockchain
from compiler.solidity_compiler import compile_contract
from evm.deploy import deploy_contract, execute_contract
from agents.ai_agent import AIAgent

state = State()
chain = Blockchain(state)

alice = Wallet()
state.get_account(alice.address()).balance = 100

source = """
x = x + 1
"""

bytecode = compile_contract(source)
contract_address = deploy_contract(state, bytecode)

agent = AIAgent(alice)
agent.act(state, contract_address)

block = chain.mine()
print(block.hash())
