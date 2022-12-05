

def get_priority(element):
    if element.isupper():
        return ord(element) - ord("A") + 27
    else:
        return ord(element) - ord("a") + 1

def reorganize_rucksack(rucksack_item_lines):

    sum_priorities = 0

    for line in rucksack_item_lines:

        rucksack_size = len(line)
        compartiment_size = rucksack_size // 2
        half_rucksack_items1 = line[:compartiment_size]
        half_rucksack_items2 = line[compartiment_size:]

        half_rucksack_items1_set = set(half_rucksack_items1)
        half_rucksack_items2_set = set(half_rucksack_items2)

        shared_item = half_rucksack_items1_set.intersection(half_rucksack_items2_set)

        priority_value = get_priority(list(shared_item)[0])
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
        assert result == 157
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

