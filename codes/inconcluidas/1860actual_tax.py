from queue import *
DEBUG = False
graph, visited, tax, sum, dist, data, sum_tax, d, pred, cont = [], [] ,[], 0, 0, [], 0, [], [], 0

def dfs(u):
    global visited, graph, tax, sum, dist, data, pred, cont

    visited[ u[0] ] = True
    dist += u[1]
    print("visited",u, dist)

    for v in graph[ u[0] ]:
    	if not visited[ v[0] ] :    
            d[v[0]] = d[u[0]] + v[1]
            pred[v[0]] = u
            #print("Not visited", v, tax, d[v[0]], dist)
            dfs(v)
           
    print(u, dist, d[v[0]])
    sum += tax[u[0]-1]
   #dist += u[1]
    
    if(sum >= data[1]):
        sum -= data[1]
        tax[u[0]-1] = sum
        print("RE", sum, dist , d[pred[u[0]][0]])
        print("Voltando", u,  dist, sum, pred, tax)
    
        if(pred[u[0]][0] != -1):
            dist +=  (2*d[pred[u[0]][0]])
        print( dist)

    else:
        tax[u[0]-1] = 0
    dist += u[1]
    # dist += u[0]
    print(dist)
    print("Voltando", u,  dist, sum,  tax)
    print()

data = [int(x) for x in input().split(' ')]
tax = [int(x) for x in input().split(' ')]

graph = [-1]*(data[0]+1)
for i in range(data[0]+1):
	graph[i] = []

for i in range(data[0]-1):
	aux = [int(x) for x in input().split(' ')]

	graph[aux[0]].append((aux[1], aux[2]))
	graph[aux[1]].append((aux[0], aux[2]))

visited = [False] *(data[0]+1)
pred = [(-1, -1)]*(data[0]+1)
d = [-1]*(data[0]+1)
d[1] = 0
print(tax)
#print(graph[1][0][1], graph)
dfs((1, 0))
print(sum, dist)
