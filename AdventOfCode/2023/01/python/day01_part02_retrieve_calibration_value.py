import sys

test_file = \
"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


if '--test' in sys.argv:
    lines = test_file.split('\n')
else:
    target_file = "../input.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(target_file, 'r') as file_handler:
        lines = file_handler.readlines()  

sum_all_calibration_values = 0

valid_digits_str = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def check_digit(i, line):
    for j, s in enumerate(valid_digits_str):
        if line[i:i+len(s)] == s:
            return j+1


for line in lines:
    # Find the first and last digit in the line
    first_digit = None
    last_digit = None
    for i, s in enumerate(line):
        if s.isdigit():
            if first_digit is None:
                first_digit = int(s)
            last_digit = int(s)
        else:
            value = check_digit(i, line)
            if value:
                if first_digit is None:
                    first_digit = value
                last_digit = value

    sum_all_calibration_values += first_digit*10 + last_digit

print("Sum of all calibration values is", sum_all_calibration_values)
