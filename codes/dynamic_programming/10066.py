data, block1, block2 = [], [], []

def towersTD(i, j):
	global block1, block2, data

	if(not memo[i][j] == -1):
		return memo[i][j]

	if(i == 0 or j == 0):
		memo[i][j] = 0

	elif(block1[i-1] == block2[j-1]):
		memo[i][j] = 1 + towersTD(i-1, j-1)
	else:
		memo[i][j] = max(towersTD(i-1, j), towersTD(i, j-1))

	return memo[i][j]

def towersBU(i, j):
	global block1, block2, data

	for k in range(i):
		memo[k][0] = 0

	for k in range(j):
		memo[0][k] = 0

	for k in range(1, i+1):
		for l in range(1, j+1):

			if(block1[k-1] == block2[l-1]):
				memo[k][l] = 1 + memo[k-1][l-1]
			else:
				memo[k][l] = max(memo[k-1][l], memo[k][l-1])

	return memo[i][j]


data = [int(x) for x in input().split()]
cont = 1
while(not data[0] == 0 or not data[1] == 0 ):
	block1 = [int(x) for x in input().split()]
	block2 = [int(x) for x in input().split()]
	
	memo = [-1]*(data[0]+1)
	for i in range(data[0]+1):
		memo[i] = [-1]*(data[1]+1)

	print("Twin Towers #%d" %cont)
	#print("Number of Tiles : %d" %towersTD(data[0], data[1]))
	print("Number of Tiles : %d" %towersBU(data[0], data[1]))
	print()
	cont += 1

	data = [int(x) for x in input().split()]