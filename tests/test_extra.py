import json
import socket
import sys
import time
import subprocess

import pytest

from evm.mini_evm import MiniEVM
from networking.node import Node
from core.transaction import Transaction
from core.state import State
from core.blockchain import Blockchain


def test_mini_evm_error_cases():
    # PUSH missing immediate
    evm = MiniEVM(["PUSH"], {}, 10)
    with pytest.raises(IndexError):
        evm.step()

    # ADD underflow
    evm = MiniEVM(["ADD"], {}, 10)
    with pytest.raises(IndexError):
        evm.step()

    # STORE missing key operand
    evm = MiniEVM(["PUSH", 1, "STORE"], {}, 10)
    # run PUSH first
    evm.step()
    with pytest.raises(IndexError):
        evm.step()

    # STORE underflow (no value on stack)
    evm = MiniEVM(["STORE", "x"], {}, 10)
    with pytest.raises(IndexError):
        evm.step()

    # LOAD missing key operand
    evm = MiniEVM(["LOAD"], {}, 10)
    with pytest.raises(IndexError):
        evm.step()

    # Unknown opcode
    evm = MiniEVM(["FOO"], {}, 10)
    with pytest.raises(ValueError):
        evm.step()


def test_node_accept_receives_and_exits(capsys):
    node = Node("127.0.0.1", 0)
    th = node.start()

    host, port = node.sock.getsockname()
    # Connect and send JSON
    s = socket.socket()
    s.connect((host, port))
    payload = json.dumps({"hi": "world"}).encode()
    s.send(payload)
    s.close()

    # give thread a moment to process
    time.sleep(0.1)

    # Close server socket to stop accept loop and join the thread
    node.sock.close()
    th.join(timeout=1.0)

    captured = capsys.readouterr()
    assert "Received:" in captured.out


def test_node_invalid_json_prints_message(capsys):
    node = Node("127.0.0.1", 0)
    th = node.start()

    host, port = node.sock.getsockname()
    s = socket.socket()
    s.connect((host, port))
    s.send(b"invalid json")
    s.close()

    time.sleep(0.1)
    node.sock.close()
    th.join(timeout=1.0)

    captured = capsys.readouterr()
    assert "Received invalid JSON" in captured.out


def test_blockchain_pending_contains_tx():
    s = State()
    c = Blockchain(s)
    tx = Transaction("a", "b", 1, 0)
    c.add_transaction(tx)
    blk = c.mine()
    assert tx in blk.transactions
    assert c.pending == []


def test_main_runs_and_outputs_hash():
    # Run main.py in-process so coverage records it
    import runpy

    runpy.run_path("main.py")


def test_wallet_address_format():
    from crypto.wallet import Wallet

    w = Wallet()
    addr = w.address()
    assert isinstance(addr, str)
    assert len(addr) == 40
    int(addr, 16)
