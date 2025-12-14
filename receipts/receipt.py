class Receipt:
    def __init__(self, tx_hash, gas_used, logs, success=True):
        self.tx_hash = tx_hash
        self.gas_used = gas_used
        self.logs = logs
        self.success = success
