import queue
graph, vstd, edges, tree, data = {}, {},[], {}, []

def prim():
	global graph, vstd, edges, tree, data

	if len(graph) == 0 :	
		return
	tam = data[0]
	for i in graph:
		if(len(graph[i]) > 0):
			tam = i
		tree [i]= {}

	vstd[tam] = True
	q = queue.PriorityQueue()
	
	for i in graph[tam]:
		q.put( ( graph[tam][i] , i, tam ) )

	cost = 0
	while not q.empty() :
		e = q.get()
		if e[1] in vstd : continue
		vstd[ e[1] ] , cost = True, cost + e[0]

        #Contruindo o novo grafo -> MST 
		edges.append( (e[1],e[2]) )
		tree[ e[1] ][ e[2] ] = e[0]
		tree[ e[2] ][ e[1] ] = e[0]

		for v in graph[ e[1] ]:
			if v not in vstd:
				q.put( (graph[ e[1] ][v] , v , e[1] ) )

	print(tree)
	print(cost)
	print(edges)
	return cost , tree , edges


data = [int(x) for x in input().split()]
#print(data)

for i in range(data[0]+1):
	graph[i] = {}
#print(graph)
for i in range(data[1]):
	edge = [int(x) for x in input().split()]

	graph[edge[0]][edge[1]] =  edge[2]
	graph[edge[1]][edge[0]] = edge[2]

prim()
