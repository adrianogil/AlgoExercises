# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

def sum_multiples_3_or_5_below(below_target):
	total_sum = 0
	for n in range(0, below_target):
		if n % 3 == 0 or n % 5 == 0:
			total_sum += n

	return total_sum


if __name__ == '__main__':
	assert sum_multiples_3_or_5_below(10) == 23

	# Find the sum of all the multiples of 3 or 5 below 1000.
	print(f'The sum of all the multiples of 3 or 5 below 1000 is', sum_multiples_3_or_5_below(1000))
