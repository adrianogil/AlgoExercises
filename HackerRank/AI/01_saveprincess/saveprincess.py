#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    grid_size = n
    grid_matrix = []
    
    peach_pos = [-1, -1]
    bot_pos = [-1, -1]
    
    # print(grid)

    for i in range(n):
        line = []
        for j in range(n):
            grid_element = grid[i][j]
            line.append(grid_element)
            if grid_element == 'p':
                peach_pos = [i, j]
            elif grid_element == 'm':
                bot_pos = [i, j]
        grid_matrix.append(line)
    
    up = [-1, 0]
    down = [1, 0]
    left = [0, -1]
    right = [0, 1]

    directions = {
        "UP": up,
        "DOWN": down,
        "LEFT": left,
        "RIGHT": right   
    }

    def go(pos, direction):
        next_pos = [pos[0] + direction[0],
                    pos[1] + direction[1]]
        return next_pos

    def is_valid(pos):
        return pos[0] >= 0 and pos[0] < grid_size and \
               pos[1] >= 0 and pos[1] < grid_size
    
    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    while dist(peach_pos, bot_pos) > 0:
        min_dist = grid_size * grid_size
        min_direction = ""

        for d in directions:
            next_pos = go(bot_pos, directions[d])
            if is_valid(next_pos):
                current_dist = dist(peach_pos, next_pos)
                if current_dist < min_dist:
                    min_dist = current_dist
                    min_direction = d
        
        # Update bot pos
        bot_pos = go(bot_pos, directions[min_direction])
        # print("%s - %s" % (min_direction, bot_pos))
        print("%s" % (min_direction))


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)