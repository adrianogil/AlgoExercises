

def move_stacks(lines):

    first_stack_line = ""

    initial_configuration_processed = False

    stacks = []
    total_stacks = -1

    for line in lines:
        line = line.replace("\n", "")

        # Process initial configuration
        if not initial_configuration_processed:
            if total_stacks == -1:
                total_stacks = (len(line) + 1) // 4
                for i in range(0, total_stacks):
                    stacks += []

        import pdb; pdb.set_trace() # Start debugger
        

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
        assert result == "CMZ"
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

