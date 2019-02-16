from queue import *

def bfs(graph, vertex, fr, ar):
	dist, vstd = [], []

	for x in range(0,vertex+1):
		dist.append(-1)
		vstd.append(False)

	dist[ int(fr) ] = 0
	vstd[ int(fr) ] = True
	q = Queue()
	q.put( fr )

	while not q.empty():
		u = q.get()
		#print( "Vértice " + str(u) + " com distância " + str(dist[int(u)]))
		if(u == ar):
			return dist[u]
		for w in graph[ int(u) ]:
			if dist[ int(w) ] == -1 :
				dist[ int(w) ] = int(dist[int(u)]) + 1
				vstd[ int(w) ] = True
				q.put(w)

	return -1 #(dist, vstd, u)


case = int(input())

while(case > 0):
	data = input().split()
	data = [int(x) for x in data]
	graph = [-1]*(data[0]+1)
	for  i in range(data[0] + 1):
		graph[i] = []

	for i in range(data[1]):
		edge = input().split()
		edge = [int(x) for x in edge]

		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	#print(graph)

	visited = [False] *data[0]
	print(bfs(graph, data[0], 1, data[0]))

	case -= 1