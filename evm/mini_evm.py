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
            self.stack.append(self.code[self.pc])
            self.pc += 1
        elif op == "ADD":
            self.stack.append(self.stack.pop() + self.stack.pop())
        elif op == "STORE":
            self.storage[self.stack.pop()] = self.stack.pop()
        elif op == "LOAD":
            self.stack.append(self.storage.get(self.stack.pop(), 0))
        elif op == "STOP":
            return False
        return True

    def run(self):
        while self.gas > 0 and self.step():
            pass
