

def get_priority(element):
    if element.isupper():
        return ord(element) - ord("A") + 27
    else:
        return ord(element) - ord("a") + 1

def reorganize_rucksack(rucksack_item_lines):

    sum_priorities = 0

    group_size = 3
    total_group_elves = len(rucksack_item_lines) // group_size

    for i in range(0, total_group_elves):
        last_elf_rucksack_common_items = None
        for g in range(0, group_size):
            line = rucksack_item_lines[i*group_size + g]
            line = line.strip()
            current_elf_rucksack = set(line)

            if last_elf_rucksack_common_items is None:
                last_elf_rucksack_common_items = current_elf_rucksack
            else:
                last_elf_rucksack_common_items = current_elf_rucksack.intersection(last_elf_rucksack_common_items)

        shared_item = list(last_elf_rucksack_common_items)[0]
        priority_value = get_priority(shared_item)
        sum_priorities += priority_value
    return sum_priorities


if __name__ == '__main__':
    import sys
    
    test_mode = False
    if '-test' in sys.argv:
        test_mode = True
        lines = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw", 
        ]
    else:
        target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

        with open(target_file, 'r') as file_handler:
            lines = file_handler.readlines()

    result = reorganize_rucksack(lines)

    if test_mode:
        print("Got", result)
        assert result == 70
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

