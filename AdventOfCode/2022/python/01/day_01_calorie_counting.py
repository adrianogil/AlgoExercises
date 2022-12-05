import sys

target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

with open(target_file, 'r') as file_handler:
    lines = file_handler.readlines()

current_calories = 0
max_calories = 0

for index, line in enumerate(lines):
    line = line.strip()
    if line == "":
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

print("Max calories is", max_calories)
