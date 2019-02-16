
from queue import *
import time
start_time = time.clock()

def dijkstra(graph,vertices, start):
	dist = [1061109567]*(vertices+10)

	dist[start] = 0
	q = Queue()
	q.put( [start, 0] )

	while not q.empty():
		u = q.get()
		#print("V�rtice " + str(u) + " com dist�ncia " + str(dist[int(u[0])]))
		if float(u[1]) > dist[u[0]]:
			continue
		for v in graph[u[0]]:
			#print(dist[v[0]], v[1], v)
			if(dist[v[0]] > v[1] +u[1] ):
				dist[v[0]] = float(v[1] + u[1])
				q.put([v[0], dist[v[0]]])
	return dist


cases = int(input())
case = 1
while(case <= cases):
	date = [int(x) for x in input().split(' ')]

	graph = [[]]*(date[0]+10)
	for i in range(date[0]+10):
		graph[i] = []
	
	for i in range(date[1]):
		edge = [int(x) for x in input().split(' ')]

		graph[edge[0]].append((edge[1], edge[2]))
		graph[edge[1]].append((edge[0], edge[2]))

	number_orders = int(input())
	orders = [int(x) for x in input().split(' ')]
	dist = dijkstra(graph, date[0], 1)
	sum = 0
	for i in range(number_orders):
		sum += ( 2 * dist[orders[i]])

	print("caso %d:" %case, format(sum, ".0f"))
	case +=1
#print(time.clock() - start_time)