with open("input.txt", "r") as file_handler:
	lines = file_handler.readlines()

a, b = map(int, lines[0].split(" "))

print(a + b)
