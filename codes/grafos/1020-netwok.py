import queue
from queue import *
graph, vstd, edges,  data, dist, tree = {}, {}, [], [] , [], []

def prim():
	global graph, vstd, edges, data, tree
	if len(graph) == 0 :	
		return

	tam, cost = data[0], 0
	for i in graph:
		tree[i] = {}
		if( len(graph[i]) > 0):
			tam = i

	vstd[tam] = True
	q = queue.PriorityQueue()
	
	for i in graph[tam]:
		q.put( ( graph[tam][i] , i, tam ) )

	while not q.empty() :
		e = q.get()
		if e[1] in vstd : 
			continue
		vstd[ e[1] ] , cost = True, cost + e[0]
		if(e[2] < e[1]):
			edges.append((e[2],e[1]))
		else:
			edges.append((e[1], e[2]))
		tree[ e[1] ] = ( e[2]  , e[0])
		tree[ e[2] ] = ( e[1]  , e[0])

		for v in graph[ e[1] ]:
			if v not in vstd:
				q.put( (graph[ e[1] ][v] , v , e[1] ) )

	return cost , edges, tree, tam

def quickSort(vector):
	left, right, pivot_list = [], [], []

	if(len(vector) <= 1):
		return vector
	else:
		pivot = vector[0]
		for i in vector:
			if( i < pivot):
				left.append(i)
			elif(i > pivot):
				right.append(i)
			else:
				pivot_list.append(i)

		right = quickSort(right)
		left = quickSort(left)

	return left + pivot_list + right

data = [int(x) for x in input().split()]
dist, tree = [-1]*(data[0]+1), [-1]*(data[0]+1)
for i in range(data[0]+1):
	graph[i] = {}

for i in range(data[1]):
	edge = [int(x) for x in input().split()]

	graph[edge[0]][edge[1]] =  edge[2]
	graph[edge[1]][edge[0]] = edge[2]

cost, edges, tree, tam = prim()
print("########################")
print("Minimum Cost:")
print(cost)
print("########################")
print("Connections:")
edges = quickSort(edges)
for i in range(len(edges)):
	print("%d" %edges[i][0] , "%d" %edges[i][1])
print("########################")
print("Pings:")
for i in graph:
	if(i >= 1 and i <=  tam):
		if(tree[0][0] <= tam):
			print("%d:" %i , "%.3f" %(2*tree[i][1]/data[2]) )
		else:
			print("%d:" %i , "%.3f" %0 )
print("########################")