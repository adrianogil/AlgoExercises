

def get_total_pairs_contained(lines):

    total_fully_contained = 0

    for line in lines:
        line = line.strip()

        elves_sections = line.split(",")

        section1 = elves_sections[0].split('-')
        section2 = elves_sections[1].split('-')

        section1[0] = int(section1[0])
        section1[1] = int(section1[1])

        section2[0] = int(section2[0])
        section2[1] = int(section2[1])

        section1_set = set(range(section1[0], section1[1] + 1))
        section2_set = set(range(section2[0], section2[1] + 1))

        # print(section1_set)
        # print(section2_set)

        overlap = len(list(section1_set.intersection(section2_set)))
        # print(overlap)

        if overlap > 0:
            total_fully_contained += 1

    return total_fully_contained


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

    result = get_total_pairs_contained(lines)

    if test_mode:
        print("Got", result)
        assert result == 4
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

