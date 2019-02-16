from queue import *
import queue
pred= graph = []

def bfs(graph, vertex, fr, ar):
    global pred
    dist, vstd, i = [], [], 0

    for x in range(0,vertex+1):
        dist.append(-1)
        vstd.append(False)
        pred.append(-1)

    dist[ int(fr) ] = 0
    vstd[ int(fr) ] = True
    q = Queue()
    q.put( fr )

    while not q.empty() and i < 100:
        u = q.get()
        #print( "V?rtice " + str(u) + " com dist?ncia " + str(dist[int(u)]))
        
        if(u == ar):
            return 1
        for v in range(len(graph[ int(u) ])):
            
            if(vstd[v] == False and graph[u][v][1] > 0):
                #print(v , graph[u][v])
                dist[ v ] = int(dist[int(u)]) + 1
                vstd[ v ] = True
                pred[ v ] = u
                q.put(v)
        i += 1

    return 0 #(dist, vstd, u)

def fordF(source, target, tam):
    global graph
    residual_graph, max_flow = graph, 0

    while(bfs(residual_graph, tam, source, target)):

        i , path_flow = target, 100*100
        while(not i == 0):
            u = pred[i]
            path_flow = min( path_flow, residual_graph[u][i][1]) 
            i = pred[i]

        i = target
        #print(path_flow)
        while(not i == 0):
            u = pred[i]
            residual_graph[u][i][1] -= path_flow
            #residual_graph[i][u][1] += path_flow
            i = pred[i]
        max_flow += path_flow 
        #print("M", max_flow)  

    return max_flow, residual_graph

def dijkstra(graph,vertices, start, end):
    global pred
    d = [10000000]*(vertices+1)
    pred = [-1]*(vertices+1)

    d[start], i = 0, 0
    q = queue.PriorityQueue()
    q.put( (0, start) )

    while not q.empty() and i < 10000000:
        u = q.get()
        #print("V?rtice " + str(u) + " com dist?ncia " +  str(d[u[1]]))
        if( d[u[1]] < u[0]):
            continue

        for v in range(len(graph[u[1]])):
            #print(v,graph[u[1]][v])
            if(graph[u[1]][v][1] > 0 and d[u[1]] + graph[u[1]][v][2] < d[v] ):  
                d[v] = d[u[1]] + graph[u[1]][v][2]
                pred[v] = u[1]
                q.put((d[v], v))

        i += 1
    if(d[end] != 10000000):
        #print(d[end])
        return d[end]
    else:
        return -1

def search(location_city, edge):
    for j in range(len(location_city)):
        for k in range(len(location_city[j])):
            if (edge == location_city[j][k]):
                #print(j, k, location_city[j][k])
                return j


q_locations_city = int(input())
q_city = int(input())

graph , graph1 = [[0, 0]]*(q_locations_city), [[0, 0]]*(q_locations_city)
for i in range(q_locations_city):
    graph[i] = [[ 0,0 ]]*(q_locations_city)
    graph1[i] = [[ 0,0 ]]*(q_locations_city)

location_city , city = [[-1]]*(q_city), [[0, 0]]*(q_city)
for i in range(q_city):
    location_city[i] = [int(x) for x in input().split()]
    location_city[i].sort()
    city[i] = []

q_roads = int(input())
for i in range(q_roads):
    edge = [int(x) for x in input().split()]

    j = search(location_city, edge[0])
    graph[ edge[0] ][edge[1]] = [ j , edge[2], edge[3] ]
    city[j].append( edge )

data = [int(x) for x in input().split()]
print(dijkstra(graph, q_locations_city, 0, q_locations_city-1))


i = data[1]
while not i == data[0]:
    number = search(location_city, i)
    for j in city[number]:
        graph1[j[0]][j[1]] = [0, j[2], j[3] ] 
    i = pred[i]

graph = graph1
max_flow, graph = fordF(data[0], data[1], q_locations_city)
print(max_flow)
