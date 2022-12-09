
def get_visible_trees(tree_matrix_str):

    size_y = len(tree_matrix_str)
    size_x = len(tree_matrix_str[0].strip())

    # print('[day_08] get_visible_trees -' + ' size_y - ' + str(size_y) + ' size_x - ' + str(size_x))

    total_visible_tree = 2 * size_x + 2 * (size_y - 2)

    visible_trees = []
    visible_trees_pos = []

    tree_matrix = []

    for y in range(0, size_y):
        current_line = []
        tree_matrix.append(current_line)
        
        for x in range(0, size_x):
            current_line.append(int(tree_matrix_str[y][x]))
    
    # print(tree_matrix)

    trees_params = {
        'max_tree_size': -1
    }

    def check_tree(x,y):
        current_tree_height = tree_matrix[y][x]
        if current_tree_height > trees_params['max_tree_size']:
            trees_params['max_tree_size'] = current_tree_height
            pos = "(%d,%d)" % (x,y)
            # print("Found visible tree %s - height %d" % (pos, current_tree_height))
            if pos not in visible_trees:
                visible_trees.append(pos)
                visible_trees_pos.append((x,y))

    # print("Left to Right")
    for y in range(1, size_y-1):

        # Left to Right
        
        trees_params['max_tree_size'] = tree_matrix[y][0]
        for x in range(1, size_x - 1):
            # print("(%d,%d) - max_tree_size - %d - height - %d" % (x, y, trees_params['max_tree_size'], tree_matrix[y][x]))
            check_tree(x,y)
    
    # print("Right to Left")
    for y in range(1, size_y - 1):
        # Right to Left
        trees_params['max_tree_size'] = tree_matrix[y][-1]
        for x in range(size_x - 2, 0, -1):
            # print("(%d,%d) - max_tree_size - %d - height - %d" % (x, y, trees_params['max_tree_size'], tree_matrix[y][x]))
            check_tree(x,y)

    # print("Up to Down")
    for x in range(1, size_x - 1):
        # Up to Down
        trees_params['max_tree_size'] = tree_matrix[0][x]
        for y in range(1, size_y - 1):
            # print("(%d,%d) - max_tree_size - %d - height - %d" % (x, y, trees_params['max_tree_size'], tree_matrix[y][x]))
            check_tree(x,y)

    # print("Down to Up")
    for x in range(1, size_x - 1):
        # Down to Up
        trees_params['max_tree_size'] = tree_matrix[-1][x]
        for y in range(size_y - 2, 0, -1):
            # print("(%d,%d) - max_tree_size - %d - height - %d" % (x, y, trees_params['max_tree_size'], tree_matrix[y][x]))
            check_tree(x,y)

    # print(visible_trees)

    total_visible_tree += len(visible_trees)

    best_scenic_score = 0

    print(visible_trees_pos)

    for pos in visible_trees_pos:
        px = pos[0]
        py = pos[1]
        scenic_score = 1
        tree_height = tree_matrix[py][px]

        # Left to Right 
        direction_score = 0   
        for x in range(px+1, size_x):
            direction_score += 1
            current_tree_height = tree_matrix[py][x]
            # print("(%d,%d) - tree_height - %d - height - %d" % (x, py, tree_height, current_tree_height))
            if current_tree_height >= tree_height or x == size_x -1:
                scenic_score *= direction_score
                print(direction_score)
                break
        
        # Right to Left
        direction_score = 0
        for x in range(px-1, -1, -1):
            direction_score += 1
            current_tree_height = tree_matrix[py][x]
            if current_tree_height >= tree_height or x == 0:
                scenic_score *= direction_score
                print(direction_score)
                break

        # Up to Down
        direction_score = 0
        for y in range(py+1, size_y):
            direction_score += 1
            current_tree_height = tree_matrix[y][px]
            if current_tree_height >= tree_height or y == size_y - 1:
                scenic_score *= direction_score
                print(direction_score)
                break
        
        # Down to Up
        direction_score = 0
        for y in range(py-1, -1, -1):
            direction_score += 1
            current_tree_height = tree_matrix[y][px]
            if current_tree_height >= tree_height or y == 0:
                scenic_score *= direction_score
                print(direction_score)
                break

        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

    return best_scenic_score


if __name__ == '__main__':
    import sys
    
    test_mode = False
    if '-test' in sys.argv:
        test_mode = True
        target_file = "test_input.txt"
    else:
        target_file = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(target_file, 'r') as file_handler:
        lines = file_handler.readlines()

    result = get_visible_trees(lines)

    if test_mode:
        print("Got", result)
        assert result == 8
        print("\nCorrect Result!")
    else:
        print("Result is ", result) 

