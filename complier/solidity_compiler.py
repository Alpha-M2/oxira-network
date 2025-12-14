def compile_contract(source_code: str):
    bytecode = []

    for line in source_code.splitlines():
        line = line.strip()
        if "x = x + 1" in line:
            bytecode += ["LOAD", "x", "PUSH", 1, "ADD", "STORE"]

    bytecode.append("STOP")
    return bytecode
