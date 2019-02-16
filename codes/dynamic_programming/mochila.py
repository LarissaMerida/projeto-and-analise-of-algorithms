data, items, weight, memo = [] , [] ,  [], []


def mochila_TD(i, cap):
	global data, items, weight, memo
	if(not memo[i][cap] == -1 ):
		return memo[i][cap]

	if(i == data[0] or cap == 0):
		memo[i][cap] = 0

	elif(weight[i] > cap):
		memo[i][cap] = mochila_TD(i+1, cap)
	else:
		memo[i][cap] = max(items[i] + mochila_TD(i+1, cap- weight[i]), mochila_TD(i+1, cap))
	return memo[i][cap]

def mochila_BU():
	global data, items, weight, memo

	for c in range(data[1] +1):
		for i in range(data[0] ,0, -1):
			if(c == 0 or i == data[0]):
				memo[i][c] = 0
			elif(weight[i] > c):
				memo[i][c] = memo[i+1][c]
			else:
				memo[i][c] = max(items[i]+ memo[i+1][c-weight[i]], memo[i+1][c])
	return memo[i][c]

data = [int(x) for x in input().split()]
items = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]

memo = [-1]*(data[0]+1)
for i in range(data[0]+1):
	memo[i] = [-1]*(data[1]+1)

#print(mochila_BU())
print(mochila_TD(0, data[1]))

