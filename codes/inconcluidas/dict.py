
from queue import *
Max = 1000
pred = []

def bfs(graph, vertex, fr, ar):
    global pred
    dist, vstd = [], []

    for x in range(0,vertex+1):
        dist.append(-1)
        vstd.append(False)
        pred.append(-1)

    dist[ int(fr) ] = 0
    vstd[ int(fr) ] = True
    q = Queue()
    q.put( fr )

    while not q.empty():
        u = q.get()
        #print( "Vértice " + str(u) + " com distância " + str(dist[int(u)]))
        
        if(u == ar):
            return 1
        for v in range(len(graph[ int(u) ])):
           # print(v , graph[u][v])
            if(vstd[v] == False and graph[u][v][1] > 0):
                dist[ v ] = int(dist[int(u)]) + 1
                vstd[ v ] = True
                pred[ v ] = u
                q.put(v)

    return 0 #(dist, vstd, u)

def fordF(source, target, tam):
    global graph
    residual_graph, max_flow = [-1]*(tam), 0
    for i in range(tam):
        residual_graph[i] = graph[i]

    print(residual_graph)
    #print(bfs(residual_graph, target, 0, target))
    while(bfs(residual_graph, tam, 0, target)):
        #print("pred", pred)

        i , path_flow = target, 100*100
        while(not i == 0):
            u = pred[i]
            path_flow = min( path_flow, residual_graph[u][i][1]) 
            i = pred[i]
        #print(path_flow, i)

        i = target
        while(not i == 0):
            u = pred[i]
           #print(u, i)
            residual_graph[u][i][1] -= path_flow
            residual_graph[i][u][1] += path_flow
            i = pred[i]
        max_flow += path_flow   
        
    
    #for i in residual_graph:
    #   print(i)
    #print(residual_graph)
    return max_flow, residual_graph


#cases = int(input())

#case = 0
#while(case < cases):
n = int(input())
edge = [-1]*(n)
for i in range(n):
    edge[i] = input().split()
print(edge)
tam = len(max(edge))-1

graph, dict =  [[-1,-1]]*(2*tam+2), {}
for i in range(2*tam+2):
    graph[i] = [[-1,-1]]*(2*tam+2)

k= n+1
for i in range(n):
   # edge = input().split()
    graph[0][int(edge[i][0])] = [0, 1]

    for j in range(1, len(edge[i])):
        edge[i][j] = edge[i][j].title()

        if(i == 0 or edge[i][j][0] not in dict):
            dict[edge[i][j][0]] = k
            k +=1
            print(edge[i][j][0], dict[edge[i][j][0]])
            graph[int(edge[i][0]) ][ dict[edge[i][j][0]] ] = [edge[i][j], 1]
            graph[dict[edge[i][j][0]]][ 2*tam ] = [edge[i][j], 1]
        else:
            graph[int(edge[i][0]) ][ dict[edge[i][j][0]] ] = [edge[i][j], 1]
            graph[dict[edge[i][j][0]]][ 2*tam ] = [edge[i][j], 1]


#print(k, minimal)  
#for i in range(len(graph)):
#   print(graph[i])

max_flow , graph = fordF(0, 2*tam , 2*tam+2)
print(max_flow, graph)

for i in range(len(graph)):
   print(graph[i])


for i in range( len(graph)):
    for j in graph[i]:
        if(not j[0] == -1 and not j[0] == 0) and j[1] == 0:
            print(j[0])

#   case += 1