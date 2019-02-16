x, y = [], []

def lcs_TD(i, j):
	global x, y
	if(not memo[i][j] == -1):
		return memo[i][j]

	if(i == 0 or j== 0):
		memo[i][j] = 0

	elif( x[i-1] == y[j-1]):
		memo[i][j] =  1 + lcs_TD(i-1, j-1)
	
	else:
		memo[i][j] = max(lcs_TD(i-1, j), lcs_TD(i, j-1))

	return memo[i][j]

def lcs_BU(i, j):
	global x, y

	for k in range(len(x)):
		memo[k][0] = 0
	for k in range(len(y)):
		memo[0][k] = 0
	
	for k in range(1, i+1):
		for l in range(1, j+1):
			if(x[k-1] == y[l-1]):
				memo[k][l] = 1 + memo[k-1][l-1]
			else:
				memo[k][l] = max(memo[k][l-1], memo[k-1][l])
	return memo[i][j]


x = input().split()
y = input().split()

print(x)
print(y)

memo = [-1]*(len(x)+1)
for i in range(len(x)+1):
	memo[i] = [-1]*(len(y)+1)

#print(lcs_TD(len(x), len(y)))
print(lcs_BU(len(x), len(y)))