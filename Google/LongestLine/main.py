# Given an NxN matrix of pixels that contains any number of lines which can be: vertical, horizontal, or diagonal. Find the longest one.


def find_longest_line(matrix):
    N = len(matrix)

    directions = [
        'vertical',
        'horizontal',
        'diagonal',
        'inverse_diagonal'
    ]

    line_size = {
        'vertical': N * [0],
        'horizontal':  N * [0],
        'diagonal':  ((2 * N) - 1) * [0],
        'inverse_diagonal': ((2 * N) - 1) * [0]
    }

    get_direction_function = {
        'horizontal': lambda x: x[1],
        'vertical': lambda x: x[0],
        'diagonal':  lambda x: (N-1) + (x[1]-x[0]),
        'inverse_diagonal': lambda x: x[1]+x[0] % ((2 * N) - 1)
    }

    longest_line = 0

    for x in range(0, N):
        for y in range(0, N):
            for direction in directions:
                line_direction = get_direction_function[direction]((x,y))
                
                # print(direction)
                # print(line_direction)
                # print(line_size[direction])
                if not matrix[x][y]:
                    if line_size[direction][line_direction] > longest_line:
                      longest_line = line_size[direction][line_direction]
                    line_size[direction][line_direction] = 0
                else:
                    line_size[direction][line_direction] += 1
          
    
    for direction in directions:
        for line_size_value in line_size[direction]:
            if line_size_value > longest_line:
                longest_line = line_size_value

    return longest_line


if __name__ == '__main__':
    matrix = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ]
    assert find_longest_line(matrix) == 4

    matrix = [
        [0, 0, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert find_longest_line(matrix) == 3

    matrix = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert find_longest_line(matrix) == 4

    matrix = [
        [1, 0, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]
    assert find_longest_line(matrix) == 5

