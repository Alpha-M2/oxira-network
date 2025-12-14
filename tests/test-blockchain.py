from core.state import State
from core.blockchain import Blockchain


def test_block_mining():
    state = State()
    chain = Blockchain(state)
    block = chain.mine()
    assert block.index == 1
