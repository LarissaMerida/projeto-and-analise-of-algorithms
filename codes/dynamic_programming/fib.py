#O(2^(n/2))
def fib(n):
	f = [-1]*(n+1)
	f[0] = 0
	f[1] = 1
	print(f)

	for i in range(2, n+1):
		f[i] = f[i-1] + f[i-2]

	print(f)
	return f[n]



#Top down
def fib_TD(n, memo):

	if(memo[n] != -1):
		print("Memo[n] != -1", n)
		return memo[n]

	if(n <= 2):
		print("n <= 2")
		f = 1
	else:
		f = fib_TD(n-1, memo) + fib_TD(n-2, memo)
	memo[n] = f
	return memo[n]

# Bottom up
def fib_BU(n, memo):
	memo[0] = 0
	memo[1] = 1

	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[n]

n = int(input())
print(fib(n))

#memo = [-1]*(n+1)
#print(fib_BUI(n, memo))
