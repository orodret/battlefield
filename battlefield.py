def get_line(body, count):
	result = body
	for i in range(count-1):
		result = result + body[1:]
	return result


def print_row(values):
	length = len(values)
	header = get_line("+-----+", length)
	empty = get_line("|     |", length)
	print(header)
	print(empty)
	for i in values:
		print('|{:^5}'.format(i), end='')
	print('|')
	print(empty)
	return header


width = int(input("Width?:"))
height = int(input("Height?:"))

battlefield = [[w for w in range(width)] for h in range(height)]

for r in battlefield:
	header = print_row(r)
print(header)

