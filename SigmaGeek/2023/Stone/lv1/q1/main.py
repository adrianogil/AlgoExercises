import numpy as np
import json


UNKNOWN_CELL = 2
LIVE_CELL = 1
DEAD_CELL = 0


class AutomataMaze:
    
    def __init__(self, initial_state, size_x, size_y):
        self.maze_states = [initial_state]
        self.size_x = size_x
        self.size_y = size_y

    def get_cell_value(self, x, y, t):
        current_maze_t = len(self.maze_states)
        if t >= current_maze_t:
            # add new maze states
            for new_t in range(current_maze_t, t + 1):
                self.maze_states.append([UNKNOWN_CELL] * (self.size_x * self.size_y))
                self.maze_states[new_t][0] = 1
                self.maze_states[new_t][self.size_x * self.size_y - 1] = 1
    
        return self.calculate_cell_value(x, y, t)

    def calculate_cell_value(self, x, y, t):
        i = y * self.size_x + x

        if t <= 0:
            return self.maze_states[0][i]
        if self.maze_states[t][i] != UNKNOWN_CELL:
            return self.maze_states[t][i]

        last_cell_value = self.get_cell_value(x, y, t - 1)

        # Calculate live and dead neighbor cells
        live_neighbors = 0
        dead_neighbors = 0

        cell_value = LIVE_CELL
        for k in range(0, 9):
            xk = (k % 3) - 1
            yk = (k // 3) - 1

            xn = x + xk
            yn = y + yk

            if (xk != 0 or yk != 0) and xn >= 0 and xn < self.size_x and yn >= 0 and yn < self.size_y:
                neightbor_value = self.get_cell_value(xn, yn, t - 1)
                # print(neightbor_value)
                if neightbor_value == LIVE_CELL:
                    live_neighbors += 1
                if neightbor_value == DEAD_CELL:
                    dead_neighbors += 1
            elif (xk != 0 or yk != 0):
                live_neighbors += 1
        if last_cell_value == LIVE_CELL and dead_neighbors in [2,3]:
            cell_value = DEAD_CELL
        elif last_cell_value == DEAD_CELL and dead_neighbors <= 6 and live_neighbors <= 4:
            cell_value = DEAD_CELL

        self.maze_states[t][i] = cell_value
        return cell_value

    def find_path(self, initial, target):
        
        initial_x = initial % self.size_x
        initial_y = initial // self.size_x

        target_pos_x = target % self.size_x
        target_pos_y = target // self.size_x

        current_t = 0

        current_pos_list = [
            {
                "pos": [initial_x, initial_y, current_t],
                "path": []
            }
        ]
        max_pos_list_size = self.size_x * self.size_y + 1
        target_pos = [target_pos_x, target_pos_y]

        best_pos_distance = 0

        max_path_repetition = 4
        max_t = 10000000
        while current_t < max_t:
            current_t += 1

            next_pos_list = []

            # Positions follows this format: x, y, t
            possible_movements = { 
                "up":    [ 0,  1, 1],
                "down":  [ 0, -1, 1],
                "left":  [-1,  0, 1],
                "right": [ 1,  0, 1],
            }

            print("Movements analized: ", len(current_pos_list), " (t ", current_t, ")")
            for pd in current_pos_list: 
                print(pd)
            for pos in current_pos_list:
                for mov in possible_movements:
                    next_pos = self.vecsum(pos["pos"], possible_movements[mov])
                    if self.is_valid_pos(next_pos):
                        next_pos_data = {
                            "pos": next_pos,
                            "path": pos["path"] + [next_pos],
                            "dist": self.sqrdist(next_pos, target_pos)
                        }
                        if next_pos[0] == target_pos[0] and next_pos[1] == target_pos[1]:
                            return next_pos_data["path"]
                        # Check if position already exists
                        if not [p for p in next_pos_list if p["pos"][0] == next_pos[0] and p["pos"][1] == next_pos[1]]:
                            # Check if position is too much repeated in the past
                            path_repetion = len([p for p in next_pos_data["path"][-10:] \
                                if p[0] == next_pos[0] and p[1] == next_pos[1]])
                            if path_repetion <= max_path_repetition:
                                next_pos_list.append(next_pos_data)
            if len(next_pos_list) > max_pos_list_size:
                next_pos_list = sorted(next_pos_list, key=lambda x: x["dist"])
                next_pos_list = next_pos_list[:max_pos_list_size]
            current_pos_list = next_pos_list
            import pdb; pdb.set_trace() # Start debugger

        return False
        

    def is_valid_pos(self, pos):
        return pos[0] >= 0 and pos[0] < self.size_x and \
               pos[1] >= 0 and pos[1] < self.size_y and \
               pos[2] >= 0 and \
               self.get_cell_value(*pos)

    def vecsum(self, v1, v2):
        vs = []
        for i in range(0, len(v1)):
            vs.append(v1[i] + v2[i])
        return vs

    def sqrdist(self, v1, v2):
        return (v1[0] - v2[0]) * (v1[0] - v2[0]) + (v1[1] - v2[1]) * (v1[1] - v2[1])

    def print_maze(self, t):
        print_state(self.maze_states[t], self.size_x, self.size_y)


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
        elif not state[i] and live_neighbors <= 4:
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
    with open('mazestates.json', 'r') as f:
        maze_data = json.load(f)

    next_state = maze_data["states"][0]["state"]
    size_x = maze_data["mazeSizeX"]
    size_y = maze_data["mazeSizeY"]
    print("State ", 0)
    print_state(next_state, maze_data["mazeSizeX"], maze_data["mazeSizeY"])

    maze = AutomataMaze(next_state, size_x, size_y)
    path = maze.find_path(0, maze_data["mazeSizeX"] * maze_data["mazeSizeY"] - 1)

    # Run Automata
    # next_state = get_next_state(maze_data["states"][1]["state"], maze_data["mazeSizeX"], maze_data["mazeSizeY"])
    # print_state(maze_data["states"][1]["state"], maze_data["mazeSizeX"], maze_data["mazeSizeY"])
    # print("Next:")
    # print_state(next_state, maze_data["mazeSizeX"], maze_data["mazeSizeY"])

    # for t in range(1, 10):
    #     print("State ", t)
    #     next_state = get_next_state(next_state, size_x, size_y)
    #     print_state(next_state, maze_data["mazeSizeX"], maze_data["mazeSizeY"])
    #     print()

