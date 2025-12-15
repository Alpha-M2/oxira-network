from agents.ai_agent import AIAgent
from client.stateless import StatelessClient
from consensus.pos import Validator, Casper
from core.transaction import Transaction
from core.state import State
from compiler.solidity_compiler import compile_contract
from evm.deploy import deploy_contract
from networking.mempool import Mempool
from networking.messages import Message
from networking.node import Node
from receipts.receipt import Receipt
from receipts.logs import Log
from rollup.l2 import Rollup, verify_rollup
from trie.mpt import MerklePatriciaTrie
from crypto.wallet import Wallet


def test_ai_agent_executes_contract():
    w = Wallet()
    s = State()
    code = compile_contract("x = x + 1")
    addr = deploy_contract(s, code)
    s.get_account(addr).storage["x"] = 0

    agent = AIAgent(w)
    agent.act(s, addr)

    assert s.get_account(addr).storage["x"] == 1


def test_stateless_client_verify():
    class Proof:
        def __init__(self, root_hash):
            self.root_hash = root_hash

    client = StatelessClient()
    p = Proof("abc")
    assert client.verify("abc", p)
    assert not client.verify("def", p)


def test_casper_finalization():
    v1 = Validator("a", 10)
    v2 = Validator("b", 30)
    casper = Casper()
    casper.vote(v1, "blk")
    casper.vote(v2, "blk")
    assert casper.finalized("blk", total_stake=50)


def test_transaction_sign_hash():
    w = Wallet()
    tx = Transaction("a", "b", 5, 0)
    h = tx.hash()
    assert isinstance(h, str)
    tx.sign(w)
    assert tx.signature is not None


def test_mempool_and_message_and_node():
    m = Mempool()
    tx1 = Transaction("a", "b", 1, 0, gas=100)
    tx2 = Transaction("a", "b", 2, 0, gas=10)
    m.add(tx1)
    m.add(tx2)
    sel = m.select()
    assert sel[0].gas >= sel[1].gas

    msg = Message(Message.NEW_TX, {"tx": "x"})
    assert msg.kind == Message.NEW_TX

    n = Node("127.0.0.1", 0)
    # socket should be bound; just close to clean up
    n.sock.close()


def test_receipts_and_rollup_and_trie():
    r = Receipt("h", 10, [Log("a", "d")], True)
    assert r.tx_hash == "h"

    roll = Rollup()
    roll.submit("t1")
    h = roll.commit()
    assert verify_rollup(h, roll.batch)

    t = MerklePatriciaTrie()
    t.insert("a", 1)
    t.insert("ab", 2)
    h1 = t.root_hash()
    # deterministic
    h2 = t.root_hash()
    assert h1 == h2
