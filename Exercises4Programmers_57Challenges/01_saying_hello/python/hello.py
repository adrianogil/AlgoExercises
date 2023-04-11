# The “Hello, World” program is the first program you learn
# to write in many languages, but it doesn’t involve any input.
# So create a program that prompts for your name and prints a greeting using your name.
# Example Output
#       What is your name? Brian
#       Hello, Brian, nice to meet you!


def hello():
	print("What is your name?")
	name = input("> ")
	print(f"Hello, {name}, nice to meet you!")


if __name__ == '__main__':
	import sys
	hello()
