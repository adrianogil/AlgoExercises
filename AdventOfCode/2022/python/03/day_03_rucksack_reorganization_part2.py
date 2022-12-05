

def get_total_pairs_not_fully_contained(rucksack_item_lines):

    
    return 0


if __name__ == '__main__':
    import sys
    
    test_mode = False
    if '-test' in sys.argv:
        test_mode = True
        lines = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8",
        ]
    else:
        target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

        with open(target_file, 'r') as file_handler:
            lines = file_handler.readlines()

    result = get_total_pairs_not_fully_contained(lines)

    if test_mode:
        print("Got", result)
        assert result == 2
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

