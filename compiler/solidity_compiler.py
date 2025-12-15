def compile_contract(source_code: str):
    bytecode = []

    for line in source_code.splitlines():
        line = line.strip()
        if "x = x + 1" in line:
            # LOAD key, PUSH 1, ADD, STORE key
            bytecode += ["LOAD", "x", "PUSH", 1, "ADD", "STORE", "x"]

    bytecode.append("STOP")
    return bytecode
