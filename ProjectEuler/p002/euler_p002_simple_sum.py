# https://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import functools

@functools.lru_cache(maxsize=None) #128 by default
def fibonacci(x):
	if x < 2:
		return 1
	
	return fibonacci(x-1) + fibonacci(x-2)


def sum_even_fibonacci_below(below_target):
	total_sum = 0
	x = 0

	while True:
		fx = fibonacci(x)

		if fx > below_target:
			return total_sum

		if fx % 2 == 0:
			total_sum += fx

		x = x + 1

	return total_sum


if __name__ == '__main__':
	# Find the sum of all the multiples of 3 or 5 below 1000.
	print(f'The sum of all the even terms of fibonacci below than 4000000 is', sum_even_fibonacci_below(4000000))
