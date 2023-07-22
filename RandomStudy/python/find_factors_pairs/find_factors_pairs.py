def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


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
	import sys

	if len(sys.argv) > 1:
		number_list_str = sys.argv[1]
		number_list = []

		number_str = ''
		for s in number_list_str:
			if is_int(s):
				number_str += s
			else:
				number_list.append(int(number_str))
				number_str = ""
		if number_str:
			number_list.append(int(number_str))
			number_str = ""

	else:
		number_list = [1, 2, 3, 4, 5, 6]
	
	if len(sys.argv) > 2:
		target = int(sys.argv[2])
	else:
		target = 12		
	
	print(f"list: {number_list}")
	print(f"target: {target}")
	pairs = find_factor_pairs(number_list, target)
	print(f"Found the following pairs: {pairs}")
