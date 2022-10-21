
def find_primes(max_number):

	primes = []

	for i in range(2, max_number):
		if not primes:
			primes = [i]
		else:
			for p in primes:
				if i % p == 0:
					break
			else:
				primes += [i]

	return primes


if __name__ == '__main__':
	import sys
	max_number = int(sys.argv[1])
	primes = find_primes(max_number)
	print(primes)
