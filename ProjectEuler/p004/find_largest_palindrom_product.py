

def is_palindrome(number):
    """
    Check if a number is a palindrome.
    """
    number = str(number)
    return number == number[::-1]


def find_largest_palindrome_product(digits=2):
    """
    Find the largest palindrome made from the product of two n-digit numbers.
    """
    largest_palindrome = 0
    largest_palindrome_factors = []
    for i in range(10 ** (digits - 1), 10 ** digits):
        for j in range(10 ** (digits - 1), 10 ** digits):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                largest_palindrome_factors = [i, j]
    return {
        "result": largest_palindrome,
        "factors": largest_palindrome_factors
        }


if __name__ == '__main__':
    n_digit = int(input("Enter the number of digits: "))
    result = find_largest_palindrome_product(n_digit)
    print(f'The largest palindrome made from the product of two {n_digit}-digit numbers is: {result["result"]} = {result["factors"][0]} * {result["factors"][1]}')
