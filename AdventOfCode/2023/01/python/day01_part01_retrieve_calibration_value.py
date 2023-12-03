import sys

target_file = "../input.txt" if len(sys.argv) < 2 else sys.argv[1]

with open(target_file, 'r') as file_handler:
    lines = file_handler.readlines()

sum_all_calibration_values = 0

for line in lines:
    # Find the first and last digit in the line
    first_digit = None
    last_digit = None
    for s in line:
        if s.isdigit():
            if first_digit is None:
                first_digit = int(s)
            last_digit = int(s)
    sum_all_calibration_values += first_digit*10 + last_digit

print("Sum of all calibration values is", sum_all_calibration_values)
