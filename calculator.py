total = 0

file = open("contents.txt")

file_contents = file.read()

file_lines = file_contents.splitlines()

for line in file_lines:
    # Extract the operator and the two numbers from the Line
    line_parts = line.split()

    if line_parts[0] != "calc":
        continue
 
    # Extract the operator and numbers
    operator = line_parts[1]
    first_number = float(line_parts[2])
    second_number = float(line_parts[3])

    if operator == "+":
        total_number = first_number + second_number
    elif operator == "x":
        total_number = first_number * second_number
    elif operator == "/":
        total_number = first_number / second_number
    elif operator == "-":
        total_number = first_number - second_number
    else:
        total_number = 0

    total += total_number

print(f"Total of all results: {total}")