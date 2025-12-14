Building an Ethereum inspired research blockchain simulation framework in Python.

Please note that it is intended for experimenting with blockchain mechanics and local testing rather than production use.

# Run the code using:
pytest

# It supports the following features:
-1 Accounts and balances
-2 Proof-of-Work 
-3 Smart contract execution (mini_EVM)
-4 Contract deployment
-5 Compiler (Solidity-like)
-6 Rollups / L2 simulation
-7 AI agents interacting with contracts
-8 Future PoS / Casper concepts

# Full details on what each .py file does:

/block.py: Block data model and likely serialization/validation.

/blockchain.py: Chain management (block addition, validation, state application, chain head management).

/state.py: Account state, balances, nonces, storage, and state transitions.

/transaction.py: Transaction model and helpers.
-------------------------------------
/mini_evm.py: Executes transactions, smart contract calls, and maybe handles gas & opcodes.

/deploy.py: Helper to deploy contracts or create contract instances.
---------------------------------------
/pos.py: Simplified proof-of-stake block selection or chain finality logic.
----------------------------------------
/node.py: Node behavior, message handling, peers.

/mempool.py: Transaction pool behavior.

/messages.py: Message types and serialization.
----------------------------------------
wallet.py: Wallet and key utilities

solidity_compiler.py: For producing bytecode or ABI for the mini EVM.

/l2.py: Logic that builds on the core chain and EVM.
-----------------------------------------
/receipt.py, logs.py: Logs and receipts handling

/mpt.py: Merkle-patricia trie for state or receipts.
------------------------------------------
/test_blockchain.py, test_wallet.py, test-transactions.py: Unit tests for major parts

# What the whole code actually does:
The code manages a ledger of accounts, accepts transactions (signed by wallets), places them in a mempool, includes them into blocks according to a simplified consensus.

It then executes transactions via the mini EVM to update state and produce receipts/logs, and supports rollup-style L2 operations. 
The networking layer simulates broadcast among nodes in tests. Tests verify correctness of core behaviors (wallet signing, transaction processing, block creation & chain updates).
