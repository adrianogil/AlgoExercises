def find_runner_up(arr):
    max_number = -1000
    runner_up = -1000

    for i in arr:
        if i > max_number:
            runner_up = max_number
            max_number = i
        elif i > runner_up and i != max_number:
            runner_up = i

    return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    runner_up = find_runner_up(arr)

    print(runner_up)
