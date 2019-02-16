import heapq

def search(graph, vertex, fr, ar):
	dist, vstd, aux, q, pred = [],[], [], [], []

	for x in range(0,vertex+1):
		dist.append(-1), vstd.append(False), pred.append(-1)

	dist[ int(fr) ], vstd[ int(fr) ] = 0, True
	heapq.heappush(q, [0, fr])

	while not q == -1:
		u = heapq.heappop(q)

		if(u[1] == ar):
			i, time = u[1], 0.0
			while(i != fr):
				aux.append(i)
				time , i =  time+ (u[0]/30) +0.06, pred[i][1]

			aux.append(i)
			time +=  (u[0]/30)
			print("Time:" + format(time, ".2f") + "h")
			return aux
	
		for v in graph[ int(u[1]) ]:
			if dist[ int(v[1]) ] == -1 :
				dist[ int(v[1]) ] = int(dist[int(u[1])]) + int(v[0])
				vstd[ int(v[1]) ] = True
				heapq.heappush(q, v)
				pred[v[1]] = u


source = int(input())
destiny = int(input())
amount_v, amount_a = input().split(' ')
amount_a, amount_v = int(amount_a) , int(amount_v)


graph, edge, aux, dist= [-1]*(amount_v+1), [], [], [-1]*(amount_v+1)
for i in range(amount_v+1):
	graph[i] = []
	
for i in range(amount_a):
	edge = input().split()
	edge = [int(x) for x in edge]

	graph[edge[0]].append((edge[2], edge[1]))
	graph[edge[1]].append((edge[2], edge[0]))

aux = search(graph, amount_v, source,destiny)
print()
print("Seasons:")
i = len(aux)-1
while(i >= 0):
	print(aux[i])
	i  -=1


	
