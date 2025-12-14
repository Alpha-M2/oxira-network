from crypto.wallet import Wallet


def test_wallet_signature():
    wallet = Wallet()
    msg = b"hello"
    sig = wallet.sign(msg)
    assert wallet.public_key.verify(sig, msg)
