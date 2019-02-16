
from queue import *
Max = 1000
edge = data= graph = pred= []

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
            #print(v , graph[u][v])
            if(vstd[v] == False and graph[u][v] > 0):
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

    #print(residual_graph)
    #print(bfs(residual_graph, target, 0, target))
    while(bfs(residual_graph, tam, 0, target)):
        #print("pred", pred)

        i , path_flow = target, 100*100
        while(not i == 0):
            u = pred[i]
            path_flow = min( path_flow, residual_graph[u][i]) 
            i = pred[i]
        #print(path_flow, i)

        i = target
        while(not i == 0):
            u = pred[i]
           #print(u, i)
            residual_graph[u][i] -= path_flow
            residual_graph[i][u] += path_flow
            i = pred[i]
        max_flow += path_flow   
        
    
    #for i in residual_graph:
    #   print(i)
    #print(residual_graph)
    return max_flow, residual_graph

def check(i, j, letter, connect):
    global edge
    if(j > 0 and edge[i][j-1] == letter):
        connect.append([i, j-1])
    if(i > 0 and edge[i-1][j] == letter):
        connect.append([i-1, j])
    if(i < len(edge)-1 and edge[i+1][j] == letter):
        connect.append([i+1, j])
    if(j < len(edge[i])-1 and  edge[i][j+1] == letter):
        connect.append([i, j+1])
    return connect

def create_graph(i, j, connect):
    global data, graph
    v = i*data[1] + j
    for k in connect:
        #print(k)
        u = k[0]*data[1] + k[1]+1
        graph[0][u] = 1
        graph[u][v] = 1
       # print("T", u, v)
    graph[v][ data[0]*data[1]+1 ] = 1

data = [int(x) for x in input().split()]
edge , graph = [-1]*(data[0]), [0]*(data[0]*data[1]+2)

for i in range(data[0]*data[1]+2):
    graph[i] = [0]*(data[0]*data[1]+2)

for i in range(data[0]):
    edge[i] = input()

for i in range(data[0]):
    for j in range(len(edge[i])):
        connect = []
        if(edge[i][j] == 'W'):
            check(i, j, 'P', connect)
            create_graph(i, j+1, connect)
            #print(i, j, (i*data[1])+j)

max_flow, graph = fordF(0, data[0]*data[1]+1, data[0]*data[1]+2 )
print(max_flow)
#for i in range(len(graph)):
#  print(graph[i])