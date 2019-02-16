

data = [int(x) for x in input().split()]

program = [[]]*(data[1])
for i in range(data[1]):
	for j in range(data[1]*data[0]):
		in = [int(x) for x in input().split()]
		program[i].append(in)

print(program)