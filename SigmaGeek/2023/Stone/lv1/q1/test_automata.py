from automata import get_next_state, print_state

import json


with open('mazestates.json', 'r') as f:
    maze_data = json.load(f)

next_state = maze_data["states"][0]["state"]
size_x = maze_data["mazeSizeX"]
size_y = maze_data["mazeSizeY"]

total_test_states = len(maze_data["states"])

for t in range(0, total_test_states):
    print("Checking State ", t)
    print_state(next_state, maze_data["mazeSizeX"], maze_data["mazeSizeY"])
    found_error = False
    for i in range(0, size_x * size_y):
        if next_state[i] != maze_data["states"][t]["state"][i]:
            print("Error!", "Position", i, "(", i % size_x, ",", i // size_x, ") !")
            print("Expected", maze_data["states"][t]["state"][i], "and got", next_state[i])
            found_error = True
    if found_error:
        print("Expected state")
        print_state(maze_data["states"][t]["state"], maze_data["mazeSizeX"], maze_data["mazeSizeY"])
        exit(1)
    next_state = get_next_state(next_state, size_x, size_y)
