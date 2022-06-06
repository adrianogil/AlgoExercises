# https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!

def is_int(string_value):
	try:
		value = int(string_value)
	except:
		return False
	return True


def decompress_string(compressed_string):

	print('[main] decompress_string - ' + compressed_string)

	decompressed_string = ''

	current_number = ''

	nest_level = 0

	start_substring = -1
	end_substring = -1

	for i in range(0, len(compressed_string)):
		c = compressed_string[i]

		if nest_level == 0:
			if is_int(c):
				current_number += c
			elif c not in ['[', ']']:
				decompressed_string += c

		if c == '[':
			if nest_level == 0:
				start_substring = i+1
			nest_level += 1
		if c == ']':
			nest_level -= 1
			if nest_level == 0:
				end_substring = i
				substring = decompress_string(compressed_string[start_substring:end_substring])
				if current_number != '':
					decompressed_string += int(current_number) * substring
					current_number = ''

	print('[main] decompress_string - ' + compressed_string + ' - result: ' + decompressed_string)

	return decompressed_string


if __name__ == '__main__':

	assert is_int('4') == True
	assert is_int('b') == False

	compressed_string = 'ab'
	result = decompress_string(compressed_string)
	assert result == 'ab'

	compressed_string = '3[abc]'
	result = decompress_string(compressed_string)
	assert result == 'abcabcabc'

	compressed_string = '3[abc]4[ab]c'
	result = decompress_string(compressed_string)
	assert result == 'abcabcabcababababc'

	compressed_string = '10[a]'
	result = decompress_string(compressed_string)
	assert result == 'aaaaaaaaaa'

	compressed_string = '2[3[a]b]'
	result = decompress_string(compressed_string)
	assert result == 'aaabaaab'
