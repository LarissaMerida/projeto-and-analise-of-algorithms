import queue
graph, vstd, data = {}, {},[]

def prim():
	global graph, vstd, data

	if len(graph) == 0 :	
		return 0

	q = queue.PriorityQueue()
	tam = data[0]
	for i in graph:
		if(len(graph[i]) > 0):
			tam = i
			#print(i, graph[i])

	vstd[tam] = True
	for i in graph[tam]:
		#print(tam, graph[tam][i])
		q.put( ( graph[tam][i] , i, tam) )

	cost = 0
	while not q.empty() :
		e = q.get()
		if e[1] in vstd : 
			continue

		vstd[ e[1] ] , cost = True, cost + e[0]
		#print(vstd, cost)

		for v in graph[ e[1] ]:
			if v not in vstd:
				q.put( (graph[ e[1] ][v] , v , e[1] ) )
	return cost 

data = [int(x) for x in input().split()]

for i in range(data[0]+1):
	graph[i] = {}

for i in range(data[1]):
	edge = [int(x) for x in input().split()]
	graph[edge[0]][edge[1]] =  edge[2]
	graph[edge[1]][edge[0]] = edge[2]

print(prim())
