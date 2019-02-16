from queue import *
import queue
graph,data = [], []

def dijkstra(graph,vertices, start):
	d = [(10000000, 100000000)]*(vertices+1)

	d[start], i = (0, 100000000), 0
	q = queue.PriorityQueue()
	q.put( (0, start, 0) )

	while not q.empty() and i < 10000000:
		u = q.get()
		#print("V?rtice " + str(u) + " com dist?ncia " +  str(d[u[1]]))
		if( d[u[1]][0] < u[0] and d[u[1]][1] < u[0]):
			continue

		for v in graph[u[1]]:

			if(d[u[1]][1] + v[2] < d[v[1]][0] ):  
				d[v[1]] = (d[u[1]][1] + v[2], d[v[1]][1])
				q.put((d[v[1]][0], v[1], v[2]))

			if(d[u[1]][0] + v[2] < d[v[1]][1]):
				d[v[1]] = (d[v[1]][0], d[u[1]][0] + v[2]);
				q.put((d[v[1]][1], v[1], v[2] ))
		i += 1
	if(d[data[0]][0] != 10000000):
		return d[data[0]][0]
	else:
		return -1

data = [int(x) for x in input().split()]

graph = [[]]*(data[0]+1)
for i in range(data[0]+1):
	graph[i] = []

for i in range(data[1]):
	edge = [int(x) for x in input().split()]
	graph[edge[0]].append((0, edge[1], edge[2]))
	graph[edge[1]].append((0, edge[0], edge[2]))

print(dijkstra(graph, data[0], 1))
