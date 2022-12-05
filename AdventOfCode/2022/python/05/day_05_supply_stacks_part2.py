

def move_stacks(lines):

    first_stack_line = ""

    initial_configuration_processed = False

    stacks = []
    total_stacks = -1

    for line_index, line in enumerate(lines):
        line = line.replace("\n", "")

        # Process initial configuration
        if not initial_configuration_processed:
            if '[' not in line:
                initial_configuration_processed = True
                continue
            if total_stacks == -1:
                total_stacks = (len(line) + 1) // 4
                for i in range(0, total_stacks):
                    stacks.append([])

            for index, crate_value in enumerate(line):
                if crate_value not in [' ', '[', ']']:
                    stack_index = (index - 1) // 4
                    stacks[stack_index].append(crate_value)
        else:
            line = line.strip()
            if line == "":
                continue
            if "move" in line and "from" in line:
                from_index = line.index("from")
                to_index = line.index("to")
                total_crate_to_move = int(line[5:from_index])
                source_stack = int(line[from_index+5:to_index]) - 1
                destination_stack = int(line[to_index+2:]) - 1
                moved_crates = []
                for _ in range(total_crate_to_move):
                    crate = stacks[source_stack].pop(0)
                    moved_crates.append(crate)
                for crate in reversed(moved_crates):
                    stacks[destination_stack].insert(0, crate)
            else:
                continue
        
    for stack in stacks:
        first_stack_line += stack[0]

    return first_stack_line


if __name__ == '__main__':
    import sys
    
    test_mode = False
    if '-test' in sys.argv:
        test_mode = True
        lines = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]
    else:
        target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

        with open(target_file, 'r') as file_handler:
            lines = file_handler.readlines()

    result = move_stacks(lines)

    if test_mode:
        print("Got", result)
        assert result == "MCD"
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

