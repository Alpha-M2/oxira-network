# Oxira-Network

A lightweight blockchain simulator and minimal EVM prototype written in Python for learning, experimentation, and quick prototyping.

---

## Quick summary

This project implements a compact blockchain stack:

- Core blockchain primitives (blocks, mining, state) — `core/`
- A minimal stack-based VM (MiniEVM) and contract deployment — `evm/`
- A tiny high-level compiler that emits simple bytecode — `compiler/`
- Wallets and signing utilities — `crypto/`
- A small PoS-like voting stub — `consensus/`
- Networking primitives (mempool, messages, simple node) — `networking/`
- Receipts/logs and a rollup batch committer — `receipts/`, `rollup/`
- A Merkle-Patricia-like trie for deterministic state hashes — `trie/`
- Tests that exercise core functionality and edge cases — `tests/`

This repository is intentionally small and educational — it is not production-ready.

---

## Why this project is useful

- Learn blockchain fundamentals end-to-end: transaction lifecycle, state roots, and block production.
- Understand VM design (stack machine, opcodes, gas/limits) and safe execution practices (stack underflow checks, clear opcode errors).
- Practice system integration across consensus, execution, networking, and storage layers.
- Gain practical skills valuable to employers: cryptography basics (signing), test-driven development, deterministic data structures, and debugging.

---

## Getting started (local)

1. Create and activate a virtual environment (macOS / Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dev dependencies (if you don't have a requirements file installed already):

```bash
python -m pip install -U pip
python -m pip install pytest pytest-cov flake8 mypy
```

3. Run tests:

```bash
python -m pytest -q
```

4. Run the example demo (`main.py`):

```bash
python main.py
```

This demo deploys a toy contract (`x = x + 1`), executes it via an agent, mines a block, and prints the block hash.

---

## Design notes

- `MiniEVM`: a tiny stack-based interpreter with opcodes such as `PUSH`, `ADD`, `LOAD`, `STORE`, `STOP`. `LOAD` and `STORE` accept immediate key operands (string keys for storage), and the VM enforces stack underflow checks and explicit errors for malformed code.
- `compiler/solidity_compiler.py`: a small helper that turns a source snippet into bytecode tokens compatible with `MiniEVM`.
- `evm/deploy.py`: deterministic address derivation for deployed code.
- `networking/node.py`: a minimal server that receives JSON messages and prints them; updated to handle invalid JSON gracefully and to allow clean shutdowns for tests.
- Tests: the repository includes comprehensive unit tests that cover VM semantics, contract execution, networking behavior, and deterministic hashing. Current test coverage is 100%.

---

## Suggested next steps / extensions

- Implement more opcodes (JUMP, SUB, MUL, comparisons) and function call semantics.
- Add gas accounting and better error reporting (reverts, stack traces).
- Expand the network layer to simulate peer messaging, forks, and block propagation.
- Replace in-memory state with a persistent key-value store and snapshots.

---
## License
MIT License
