
from queue import *
Max = 1000
pred, dict = [], {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L':12, 
                    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 
                    'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

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

    #print(residual_graph)
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
k, minimal = n+1, -1

for i in range(n):
    edge[i] = input().split()
    minimal = int(edge[i][0]) if(int(edge[i][0]) > minimal) else minimal

graph =  [[-1,-1]]*(n+27)
for i in range(n+27):
    graph[i] = [[-1,-1]]*(n+27)

for i in range(n):
    graph[0][int(edge[i][0])] = [0, 1]
    
    for j in range(1, len(edge[i])):
        edge[i][j] = edge[i][j].title()
       
        graph[int(edge[i][0]) ][ dict[edge[i][j][0]]] = [edge[i][j], 1]
        graph[dict[edge[i][j][0]]][ 2*minimal+1 ] = [edge[i][j], 1]

        k = dict[edge[i][j][0]] if( dict[edge[i][j][0]] > k) else k

#print(k, minimal)  
#for i in range(len(graph)):
#   print(graph[i])

max_flow , graph = fordF(0, 2*minimal+1 , n+27)
print(max_flow)

for i in range(len(graph)):
   print(graph[i])


for i in range( len(graph)):
    for j in graph[i]:
    	if(max_flow):
            if(not j[0] == -1 and not j[0] == 0) and j[1] == 0:
                print(j[0])
                max_flow -= 1

#   case += 1