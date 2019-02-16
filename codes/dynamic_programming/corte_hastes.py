import math 
import sys
sys.setrecursionlimit(15000000)

def cutting_rodBU(n, memo, valor): 
   valor[0] = 0;

   for i in range(1,n+1):
       max_val = -1;

       for j in range(i):
         aux = memo[j] + valor[i-(j+1)]
         #print(aux, max_val)
         if aux > max_val:
          max_val = aux
       valor[i] = max_val;

   return valor[n];

def cutting_rod_TD(n, memo, valor):
	if( not memo[n] == -1 ):
		return memo[n]

	if(n <= 0):
		return 0
	else:
		best = -1
		for i in range(1, n+1):
			m = cutting_rod_TD(n-i, memo, valor)
			if(best <  valor[i-1] + m):
				best =  valor[i-1] + m
	
	memo[n] = best
	return best


tam = int(input())
while(tam != 0):
	rod = [0]*(tam)
	for i in range(tam):
		rod[i] = int(input())

	memo = [-1]*(tam+1)
	print(cutting_rod_R(tam, memo,rod))
	tam = int(input())
