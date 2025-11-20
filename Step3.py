def calculate(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "x":
        return a * b
    elif op == "/":
        if b == 0:
            return 0
        return a // b
    else:
        raise ValueError("Invalid operator")



with open("contents2.txt") as f:
    lines = f.read().splitlines()

visited = set()

line_number = 1 

while True:

    statement = lines[line_number - 1]

    if statement in visited:
        print(f"STOPPED on line {line_number}: {statement}")
        break

    visited.add(statement)

    parts = statement.split()

    if parts[0] == "goto":

        if parts[1] != "calc":
            target_line = int(parts[1])
            line_number = target_line

        else:
            op = parts[2]
            a = int(parts[3])
            b = int(parts[4])
            result = calculate(op, a, b)
            line_number = result

    else:
        line_number += 1
