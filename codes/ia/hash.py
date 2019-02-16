DEBUG = False

def write(field, x, y, turn):
	if( field[x][y] == "_"):
		field[x][y] = turn
	else:
		print("Invalid position.")
		print()
		return -1, field
	return 1, field

def show(field):
	for i in range(3):
		print(*field[i])

def create():
	field = [[]]*3
	for i in range(3):	
		field[i] = ['_' ,'_', '_']
	return field

def check(field):
	x, o = 0, 0

	for i in range(3):
		if(field[i][i] == 'X'):
			x += 1
		if(field[i][i] == 'O'):
			o += 1
	if(DEBUG == True):
		print("1", x, o)

	if(x < 3 and o < 3):
		x, o, j = 0, 0, 2
		for i in range(3):
			if(field[i][j] == 'X'):
				x += 1
			if(field[i][j] == 'O'):
				o += 1
			j -=1
	if(DEBUG == True):
		print("2", x, o)

	if(x < 3 and o < 3):
		for i in range(3):
			x, o = 0, 0
			for k in range(3):
				if(field[i][k] == 'X'):
					x += 1
				if(field[i][k] == 'O'):
					o += 1
			if(x == 3 or o == 3):
				break;
	if(DEBUG == True):
		print("3", x, o)

	if(x < 3 and o < 3):
		for i in range(3):
			x, o = 0, 0
			for k in range(3):
				if(field[k][i] == 'X'):
					x += 1
				if(field[k][i] == 'O'):
					o += 1
			if(x == 3 or o == 3):
				break;
	if(DEBUG == True):
		print("4", x, o)

	if(x == 3):
		return "X"
	elif( o == 3):
		return "O"
	else:
		return "V"

def h(field, x, y, turn):
	op = "V"
	if(field[x][y] == "_"):
		field[x][y] = turn
	
		op = check(field)
		if(op == "V"):
			if(ok == 1):
				field[x][y] = "_"
	return op, field

def max(field):
	x, o = 0, 0

	op, field = h(field, 0, 0, "X");
	if(op == "V"):
		op, field = h(field, 0, 2, "X");
	if(op == "V"):
		op, field = h(field, 2, 0, "X");
	if(op == "V"):
		op, field = h(field, 2, 2, "X");

	if(op == "V"):
		for i in range(3):
			for j in range(3):
				if(field[i][j] == 'O'):
						if(i == 0 and field[i][2] == '_'):
							field[i][2] = "X"
						elif(i == 2 and  field[i][0] == '_'):
							field[i][0] = "X"
						elif(i == 2 and field[i-2][j] == '_'):
							field[i-2][j] = "X"
						elif(j == 0 and  field[i][j+2] == '_'):
							field[i][j+2] = "X"
						elif(j == 2 and  field[i][j-2] == '_'):
							field[i][j-2] = "X"
	return field

graph, cont, ok = [], 0, 1
field = create()
ok, field = write(field, 1, 1, 'X')
graph.append(field)
show(field)

while(cont < 4 and check(field) == "V"):
	opponent_data = input("Enter x y: ").split()
	opponent_data = [int(i) for i in opponent_data]
	ok, field = write(field, opponent_data[0], opponent_data[1], 'O')
	op = check(field)
	if(op == "X" or op == "O"):
		show(field)
		break;
	if(ok == 1):
		field = max(field)
		show(field)
		op = check(field)
		if(op == "X" or op == "O"):
			break;
		cont+=1
print()
print(check(field))