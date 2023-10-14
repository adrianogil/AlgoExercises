# https://projecteuler.net/problem=3
def find_largest_prime_factor(target_number):
    factor = 2
    while target_number > 1:
        if target_number % factor == 0:
            target_number //= factor
        else:
            factor += 1
    return factor


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <number>")
        sys.exit(1)

    try:
        target_number = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as input.")
        sys.exit(1)

    if target_number <= 1:
        print("Please provide an integer greater than 1.")
        sys.exit(1)

    largest_prime_factor = find_largest_prime_factor(target_number)
    print(largest_prime_factor)