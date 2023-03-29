import json
import sys

def get_next_state(state, size_x, size_y):
    next_state = [1]

    for i in range(1, len(state) - 1):
        xs = i % size_x
        ys = i // size_x

        current_pattern = []

        live_neighbors = 0
        dead_neighbors = 0
        next_value = 1
        for k in range(0, 9):
            xk = (k % 3) - 1
            yk = (k // 3) - 1

            xn = xs + xk
            yn = ys + yk

            if (xk != 0 or yk != 0) and xn >= 0 and xn < size_x and yn >= 0 and yn < size_y:
                it = yn * size_x + xn
                live_neighbors += state[it]
                if not state[it]:
                    dead_neighbors += 1
            elif (xk != 0 or yk != 0):
                live_neighbors += 1
        # print(dead_neighbors)
        if state[i] and dead_neighbors in [2,3]:
            next_value = 0
        elif not state[i] and (live_neighbors <= 4):
            next_value = 0
        next_state.append(next_value)
    next_state += [1]
    return next_state


def print_state(state, state_size_x, state_size_y):
    rows = state_size_y
    cols = state_size_x

    for i in range(rows):
        row = ''
        for j in range(cols):
            index = i * cols + j
            row += str(state[index]) + ' '
        row += ' - ' + str(i)
        print(row)


if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        min_t = 0
        max_t = int(sys.argv[1])
    elif len(sys.argv) > 2:
        min_t = int(sys.argv[1])
        max_t = int(sys.argv[2])
    else:
        min_t = 0
        max_t = 2

    with open('mazestates.json', 'r') as f:
        maze_data = json.load(f)

    next_state = maze_data["states"][0]["state"]
    size_x = maze_data["mazeSizeX"]
    size_y = maze_data["mazeSizeY"]

    for t in range(0, max_t + 1):
        if t >= min_t and t <= max_t:
            print()
            print("State ", t)
            print_state(next_state, maze_data["mazeSizeX"], maze_data["mazeSizeY"])
        next_state = get_next_state(next_state, size_x, size_y)
        