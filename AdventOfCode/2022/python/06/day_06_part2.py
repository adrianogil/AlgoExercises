

def get_marker(line):

    line = line[0].strip()
    line_size = len(line)

    for i in range(0, line_size - 14):

        current_possible_marker = line[i:i+14]
        current_possible_marker_set = set(current_possible_marker)

        if len(current_possible_marker_set) == 14:
            return i+14

    return 0


if __name__ == '__main__':
    import sys
    
    test_mode = False
    if '-test' in sys.argv:
        test_mode = True
        lines = [
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        ]
    else:
        target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

        with open(target_file, 'r') as file_handler:
            lines = file_handler.readlines()

    result = get_marker(lines)

    if test_mode:
        print("Got", result)
        assert result == 19
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

