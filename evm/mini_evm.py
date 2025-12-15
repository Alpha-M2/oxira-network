class MiniEVM:
    def __init__(self, code, storage, gas):
        self.code = code
        self.storage = storage
        self.stack = []
        self.pc = 0
        self.gas = gas

    def step(self):
        op = self.code[self.pc]
        self.pc += 1
        self.gas -= 1

        if op == "PUSH":
            if self.pc >= len(self.code):
                raise IndexError("PUSH missing immediate operand")
            self.stack.append(self.code[self.pc])
            self.pc += 1
        elif op == "ADD":
            # ensure there are at least two items
            if len(self.stack) < 2:
                raise IndexError("stack underflow on ADD")
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a + b)
        elif op == "STORE":
            if self.pc >= len(self.code):
                raise IndexError("STORE missing key operand")
            key = self.code[self.pc]
            self.pc += 1
            if len(self.stack) < 1:
                raise IndexError("stack underflow on STORE")
            val = self.stack.pop()
            self.storage[key] = val
        elif op == "LOAD":
            if self.pc >= len(self.code):
                raise IndexError("LOAD missing key operand")
            key = self.code[self.pc]
            self.pc += 1
            self.stack.append(self.storage.get(key, 0))
        elif op == "STOP":
            return False
        else:
            raise ValueError(f"unknown opcode: {op}")
        return True

    def run(self):
        while self.gas > 0 and self.step():
            pass
