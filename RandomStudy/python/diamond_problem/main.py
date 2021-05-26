# <>
# <..<..>> => 2
# <...<.<..>..>>>..>><..>> => 4
# <<> => 1
# >><> => 1

def diamond(input_list):
    """
        Return all diamons found
    """
    diamonds = 0
    open_diamonds = 0

    for i in input_list:
        if i == '<':
            open_diamonds += 1
        elif i == '>':
            if open_diamonds > 0:
                open_diamonds -= 1
                diamonds += 1

    return diamonds


# assert diamond("<>") == 1
# assert diamond("<..<..>>") == 2
# assert diamond("<...<.<..>..>>>..>><..>>") == 4
# assert diamond("<<>") == 1

# [1, 1, 2, 3, 4] == 1 => 2, 2 => 1, 3 => 1, 4 => 1
# [1, 1, 2, 3, 4, 5] == 1 => 2, 2 => 1, 3 => 1, 4 => 1
# [1, 1, ..., 2, 3, 3, ...]
# [[1, 1], | [1, 2]]
#
# countNumber(n, l)
# ordenada
# composta por idade de pessoas
# composta por milhões de números

def counter(input_list):
    result = {}

    for i in input_list:
        result[i] = 1 + result.get(i, 0)

    return result


def counter_bin(input_list, result):
    result['chamadas'] = 1 + result.get('chamadas', 0)

    list_size = len(input_list)

    if list_size < 1:
        return

    i = input_list[0]

    if list_size == 1:
        result[i] = 1 + result.get(i, 0)
        return result
    if input_list[0] == input_list[-1]:
        # ex:  start=1, end=1, input_list=[1,1,1,1]
        result[i] = list_size + result.get(i, 0)
        return result

    mean_element = list_size // 2

    initial_list = input_list[:mean_element]
    remain_list = input_list[mean_element:]

    counter_bin(initial_list, result)
    counter_bin(remain_list, result)

    # print(result, mean_element, list_size, input_list, initial_list, remain_list)

    return result

counter_method = counter_bin


# result = counter_method([1, 1, 2, 3, 4])
# assert result[1] == 2
# assert result[2] == 1
# assert result[3] == 1
# assert result[4] == 1

for ne in range(0, 6):

    f1 = 100 * (10 ** ne)
    f2 = 50 * (10 ** ne)
    f3 = 1 * (10 ** ne)
    f4 = 20 * (10 ** ne)

    total_elements = f1 + f2 + f3 + f4

    result = {}
    result = counter_method(f1 * [1] + f2 * [2] + f3 * [3] + f4 * [4], result)
    print(result, f1, f2, f3, f4)
    assert result[1] == f1
    assert result[2] == f2
    assert result[3] == f3
    assert result[4] == f4
    print(ne, total_elements, result['chamadas'])
