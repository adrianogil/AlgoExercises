# https://www.hackerrank.com/challenges/list-comprehensions/problem
from itertools import product


def get_cube_positions(x, y, z, n):
    all_positions = list(product(range(x + 1), range(y + 1), range(z + 1)))

    return [list(pos) for pos in all_positions if (pos[0] + pos[1] + pos[2]) != n]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    cube_positions = get_cube_positions(x, y, z, n)
    print(cube_positions)
