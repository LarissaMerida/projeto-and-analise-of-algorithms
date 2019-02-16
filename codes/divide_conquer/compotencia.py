def calculate_power(n, e):
	if(e == 0):
		return 1
	elif(e == 1):
		return n
	if(e%2 == 0):
		half = calculate_power(n, e/2)
		return (n*n)%100
	else:
		half = calculate_power(n, (e-1)/2)
		return n*half*half	 

def compotencia(n):
	power1 = calculate_power(n[0], n[0])%100
	power2 = calculate_power(n[1], n[1])%100
	if(power1 > power2):
		print(n[0])
	elif(power1 < power2):
		print(n[1])
	else:
		print('0')

n, stop = [0], 0
while stop != 1:
	try:
		n = input().split()
		n = [int(i) for i in n]
		result = compotencia(n)
	except Exception:
		stop = 1