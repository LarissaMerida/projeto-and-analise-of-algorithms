from queue import *
DEBUG = False
graph, visited, height = [], [], 5

def dfs(u):
    global visited, graph, height

    if (DEBUG):
        print(u)
    if(height != 0):
    	print("Cannibais:",int(u/10))
    	print("missionaries:",u%10)
    	print()

    visited[ u ] = True
    for v in graph[ u ]:
    	if height == 0:
    		print("Cannibais:",int(u/10))
    		print("missionaries:",u%10)
    		print()
    		return u
    	if not visited[ v ]:
        	height -=1
        	dfs(v)

amount_v = int(input())
date,graph = [],[-1]*34
for i in range(34):
	graph[i] = []

for i in range(amount_v):
	date = input().split()
	date = [int(x) for x in date]
	for j in range(1, len(date)):
		graph[date[0]].append(date[j])

vertices = 34
visited = [False] * 34
print("-- The steps are:")
print()
dfs(33)