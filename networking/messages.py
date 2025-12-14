class Message:
    NEW_TX = "NEW_TX"
    NEW_BLOCK = "NEW_BLOCK"

    def __init__(self, kind, data):
        self.kind = kind
        self.data = data
