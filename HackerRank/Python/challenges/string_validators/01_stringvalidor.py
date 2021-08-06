# https://www.hackerrank.com/challenges/string-validators/problem

def check_if_at_least_one(s, char_validation_func):
    for c in s:
        if char_validation_func(c):
            return True
    return False

if __name__ == '__main__':
    s = raw_input()
    print(check_if_at_least_one(s, lambda x: x.isalnum()))
    print(check_if_at_least_one(s, lambda x: x.isalpha()))
    print(check_if_at_least_one(s, lambda x: x.isdigit()))
    print(check_if_at_least_one(s, lambda x: x.islower()))
    print(check_if_at_least_one(s, lambda x: x.isupper()))
