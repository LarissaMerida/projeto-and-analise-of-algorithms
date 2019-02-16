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
        print( "V?rtice " + str(u) + " com dist?ncia " + str(dist[int(u)]))
        
        if(u == ar):
            return 1
        for v in range(len(graph[ int(u) ])):
            
            if(vstd[v] == False and graph[u][v][1] > 0):
                print(v , graph[u][v])
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
        print(path_flow)
        while(not i == 0):
            u = pred[i]
            residual_graph[u][i][1] -= path_flow
            residual_graph[i][u][1] += path_flow
            i = pred[i]
        max_flow += path_flow 
        print("M", max_flow)  

    return max_flow

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
            if(graph[u[1]][v][0] > 0 and d[u[1]] + graph[u[1]][v][0] < d[v] ):  
                d[v] = d[u[1]] + graph[u[1]][v][0]
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

location_city , city, connect = [[-1]]*(q_city), [[0, 0]]*(q_city), [[0, 0]]*(q_city)
for i in range(q_city):
    location_city[i] = [int(x) for x in input().split()]
    location_city[i].sort()
    city[i] = [[ 0, 0]]*(q_city)
    connect[i] = [ ]
#print(location_city)

graph  = [[0, 0]]*(q_locations_city)
for i in range(q_locations_city):
    graph[i] = [[ 0,0 ]]*(q_locations_city)

q_roads = int(input())
for i in range(q_roads):
    edge = [int(x) for x in input().split()]
    #graph[ edge[0] ][edge[1]] = edge[2:]

    if(edge[3] > 0):
        j = search(location_city, edge[0])
        k = search(location_city, edge[1])
        city[j][k] = [edge[3], edge[2]]
    else:
        j = search(location_city, edge[0])
    connect[j].append(edge)

data = [int(x) for x in input().split()]
print(dijkstra(city, q_city, 0, q_city-1))
source = search(location_city, data[0])
target = search(location_city, data[1])
#print(source, target)
#print(pred)
i, max_flow = q_city-1, 100*100
while not i == 0:
    u = pred[i]
    #print(i, city[u][i])
    #graph[u][i] = city[u][i]
    max_flow = min(max_flow, city[u][i][1])
    i = pred[i]


for j in connect[target]:
    graph[j[0]][j[1]] = [j[3], j[2] ] 
    print(j[0])


#for i in range(len(graph)):
#   print(graph[i])

#max_flow = min( fordF(source, target, q_locations_city), max_flow)
print(max_flow)