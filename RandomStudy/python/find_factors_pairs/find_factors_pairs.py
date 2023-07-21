

def find_factor_pairs(number_list, target):
	pairs = []

	factors = []

	for i in number_list:
		if target % i == 0:
			if (target // i) in factors:
				pairs.append((i, (target // i)))
			factors.append(i)

	return pairs

if __name__ == '__main__':
	number_list = [1, 2, 3, 4, 5, 6]
	target = 12
	pairs = find_factor_pairs(number_list, target)
	print(pairs)
