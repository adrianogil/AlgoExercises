import sys

test_file = \
"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


if '--test' in sys.argv:
    lines = test_file.split('\n')
else:
    target_file = "../input.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(target_file, 'r') as file_handler:
        lines = file_handler.readlines()  

sum_all_game_id_possible = 0

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def check_cubes(cubes):
    # example: ['3', 'blue']
    count, color = cubes
    count = int(count)
    if color == 'red':
        return count <= MAX_RED
    elif color == 'green':
        return count <= MAX_GREEN
    elif color == 'blue':
        return count <= MAX_BLUE
    else:
        raise Exception("Unknown color: ", color)

def check_cubes_set(cubes_set):
    # example: [['3', 'blue'], ['4', 'red']]
    for cubes in cubes_set:
        if not check_cubes(cubes):
            return False
    return True


for line in lines:
    game_id, *game_data = line.split(':')
    game_id = int(game_id.split(' ')[1])
    game_data = game_data[0].split(';')
    game_data = [x.strip() for x in game_data]
    game_data = [x.split(',') for x in game_data]
    game_data = [[y.strip() for y in x] for x in game_data]
    game_data = [[y.split(' ') for y in x] for x in game_data]
    game_data = list(map(check_cubes_set, game_data))
    # print(game_id, game_data)
    sum_all_game_id_possible += game_id if all(game_data) == True else 0

print("Sum of all game IDs that are possible ", sum_all_game_id_possible)
