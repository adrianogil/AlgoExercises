def print_matrix(matrix):
    total_lines = len(matrix)
    total_cols = len(matrix[0])

    for line in range(0, total_lines):
        line_str = ""
        for col in range(0, total_cols):
            if matrix[line][col] is None:
                line_str += " None"
            else:
                line_str += " %4.0f" % (matrix[line][col])
        print(line_str)
