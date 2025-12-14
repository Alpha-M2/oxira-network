class StatelessClient:
    def verify(self, state_root, proof):
        return proof.root_hash == state_root
