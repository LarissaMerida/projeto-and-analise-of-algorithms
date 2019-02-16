import queue
import math

DEBUG = False
graph, visited = [], []

def dfs(u):
    global visited, graph
    visited[ u ] = True 
    #print("visited",u)

    for v in graph[ u ]:
    	if not visited[ v ] : 
            #print("Not visited", v)
            dfs(v)
 

data = [int(x) for x in input().split()]

graph , edge, visited =[[]]*(data[0]), [-1]*(data[0]), [False]*(data[0])
for i in range(data[0]):
	graph[i] = []

for i in range(data[0]):
	edge[i] = [ int(x) for  x  in input().split()]

for i in range(data[0]):
	for j in range(data[0]):
		if( i == j):
			continue;

		d = ((edge[j][0]-edge[i][0])**2 + (edge[j][1]-edge[i][1])**2)**(1/2)
		if(d <= data[1]):
			graph[i].append(j)

dfs(0)
impossible = 0
for i in visited:
	if(i == False):
		print("N")
		impossible = 1
		break

if(impossible == 0):
	print("S")
