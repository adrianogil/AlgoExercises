""" Simplified version of Emil problem """
import sys
import utils
from pyutils.decorators import debug


def get_best_answer(suitable_answers):
    min_size = 10000000

    for i in range(0, len(suitable_answers)):
        if len(suitable_answers[i]) < min_size:
            min_size = len(suitable_answers[i])

    best_answers = []

    for i in range(0, len(suitable_answers)):
        if len(suitable_answers[i]) == min_size:
            best_answers.append(suitable_answers[i])

    best_answers = sorted(best_answers)

    return best_answers[0]


# @debug
def verify_pair_matching(left_pair, right_pair):
    if left_pair is None or right_pair is None:
        return False

    if len(left_pair) < len(right_pair):
        return right_pair.startswith(left_pair)
    elif len(left_pair) == len(right_pair):
        return left_pair == right_pair
    else:
        return left_pair.startswith(right_pair)


def emil_problem(left_pair, right_pair):
    total_pairs = len(left_pair)

    diff_matrix = [[None] * total_pairs for t in range(0, total_pairs)]
    index_matrix = [[-1] * total_pairs for t in range(0, total_pairs)]
    str_matrix = [[""] * total_pairs for t in range(0, total_pairs)]

    suitable_answers = []

    for line in range(0, total_pairs):
        for col in range(0, total_pairs):
            # print("%s,%s" % (line, col))
            if line == 0:
                diff_matrix[line][col] = len(left_pair[col]) - len(right_pair[col])
                str_matrix[line][col] = [left_pair[col], right_pair[col]]
                index_matrix[line][col] = col
            else:
                best_diff = 0
                best_pairs = None

                for last_line_col in range(0, total_pairs):
                    if last_line_col != col:
                        rev_line = line - 1
                        pairs = None
                        used_pair = False

                        while rev_line >= 0 and (pairs is None or pairs[0] is None or pairs[1] is None):
                            pairs = str_matrix[rev_line][last_line_col]
                            rev_line -= 1

                        lcol = last_line_col
                        while rev_line >= 0:
                            lindex = index_matrix[rev_line][lcol]
                            if lindex == col:
                                used_pair = True
                                break
                            else:
                                lcol = lindex
                            rev_line -= 1

                        if not used_pair and pairs is not None and pairs[0] is not None and pairs[1] is not None:
                            new_pairs = [pairs[0] + left_pair[col],
                                         pairs[1] + right_pair[col]]

                            if verify_pair_matching(new_pairs[0], new_pairs[1]):
                                diff = len(new_pairs[0]) - len(new_pairs[1])
                                if best_pairs is None:
                                    best_pairs = new_pairs
                                    best_diff = diff
                                    best_col = last_line_col
                                elif abs(diff) < abs(best_diff):
                                    best_pairs = new_pairs
                                    best_diff = diff
                                    best_col = last_line_col
                if best_pairs is None:
                    diff_matrix[line][col] = None
                    str_matrix[line][col] = None
                else:
                    diff_matrix[line][col] = best_diff
                    str_matrix[line][col] = best_pairs
                    index_matrix[line][col] = best_col
            if diff_matrix[line][col] == 0 and str_matrix[line][col][0] == str_matrix[line][col][1]:
                suitable_answers.append(str_matrix[line][col][0])

    # utils.print_matrix(diff_matrix)

    # for a in suitable_answers:
    #     print(a)

    if len(suitable_answers) == 0:
        return "IMPOSSIBLE"

    return get_best_answer(suitable_answers)


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
