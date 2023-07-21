# Function to calculate the mean percentage of factors a number in a given range has
def get_mean_numbers_of_factors(max_number=1000):

	# Initialize a variable to store the sum of percentages
	percentage_sum = 0

	for i in range(4, max_number):
		# print(i)
		total_factors = 0
		factors = []

		for j in range(1, i+1):
			if (i % j) == 0:
				total_factors += 1
				factors.append(j)
		percentage_sum += (total_factors / i)
		current_percentage_str = "%.3f" % ((100.0*percentage_sum)/(i-3),)
		print(f"N: {i} - Number of factors: {total_factors} ({current_percentage_str} %): {factors}")

	# Print the average percentage of total factors across all numbers in the range
	


if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		max_number = int(sys.argv[1])
	else:
		# If no command line argument was provided, default to 1000 as the maximum number
		max_number = 1000
	get_mean_numbers_of_factors(max_number)
