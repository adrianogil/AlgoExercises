
def find_largest_prime_factor(target_number):

	primes = []

	largest_prime_factor = 0

	for i in range(2, target_number // 2 if target_number > 4 else target_number):
		if not primes:
			primes = [i]
			if target_number % i == 0:
				largest_prime_factor = i
		else:
			for p in primes:
				if i % p == 0:
					break
			else:
				primes += [i]
				if target_number % i == 0:
					largest_prime_factor = i


	return largest_prime_factor


if __name__ == '__main__':
	import sys
	target_number = int(sys.argv[1])
	largest_prime_factor = find_largest_prime_factor(target_number)
	print(largest_prime_factor)
