""" Simplified version of Emil problem """
import sys
import utils


def emil_problem(left_pair, right_pair):
    total_pairs = len(left_pair)

    diff_matrix = [[None] * total_pairs for t in range(0, total_pairs)]
    index_matrix = [[-1] * total_pairs for t in range(0, total_pairs)]
    str_matrix = [[""] * total_pairs for t in range(0, total_pairs)]

    for line in range(0, total_pairs):
        for col in range(0, total_pairs):
            if line == 0:
                diff_matrix[line][col] = len(left_pair[col]) - len(right_pair[col])
                str_matrix[line][col] = [left_pair[col], right_pair[col]]
            # else:
            #     current_diff = len(left_pair[col]) - len(right_pair[col])

            #     min_diff = 0

            #     for last_line_col in range(0, total_pairs):


    utils.print_matrix(diff_matrix)

    return "IMPOSSIBLE"


if __name__ == '__main__':
    target_test_case_file = sys.argv[1]

    test_case_lines = []
    with open(target_test_case_file, "r") as tfile:
        test_case_lines = tfile.readlines()

    test_case_number = 1

    lines_to_read = 0
    left_pair = []
    right_pair = []

    for l in test_case_lines:
        if lines_to_read <= 0:
            lines_to_read = int(l.strip())
            left_pair = []
            right_pair = []
        else:
            lines_to_read -= 1
            pairs = l.strip().split(" ")
            left_pair.append(pairs[0])
            right_pair.append(pairs[1])
            if lines_to_read == 0:
                answer = emil_problem(left_pair, right_pair)
                print("Case %s: %s" % (test_case_number, answer))
                test_case_number += 1
