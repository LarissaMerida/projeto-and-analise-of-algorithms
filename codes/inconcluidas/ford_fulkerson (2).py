
from queue import *
Max = 40
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
        #print( "V�rtice " + str(u) + " com dist�ncia " + str(dist[int(u)]))
        
        if(u == ar):
            return 1
        for v in range(len(graph[ int(u) ])):
            
            if(vstd[v] == False and graph[u][v][1] > 0):
                #print(v , graph[u][v])
                dist[ v ] = int(dist[int(u)]) + 1
                vstd[ v ] = True
                pred[ v ] = u
                q.put(v)

    return 0 #(dist, vstd, u)

def fordF(source, target, tam):
    global graph
    residual_graph, max_flow,answer = [-1]*(tam), 0, []
    for i in range(tam):
        residual_graph[i] = graph[i]

    while(bfs(residual_graph, tam, 0, target)):

        i , path_flow = target, 100*100
        while(not i == 0):
            u = pred[i]
            path_flow = min( path_flow, residual_graph[u][i][1]) 
            i = pred[i]

        i = target
        while(not i == 0):
            u = pred[i]
            residual_graph[u][i][1] -= path_flow
            residual_graph[i][u][1] += path_flow
            if(not residual_graph[u][i][0] == 0 ):
                answer.append([ dict[  residual_graph[u][i][0][0] ] , max_flow , residual_graph[u][i]])
            #print(residual_graph[u][i], max_flow)
            i = pred[i]
        max_flow += path_flow   

    return max_flow, residual_graph, answer

cases = int(input())
case = 1
while(case <= cases):
    n = int(input())
    edge, minimal , graph, answer = [[-1]]*(Max), -1,[[0, 0]]*(Max), []

    for i in range(Max):
        graph[i] = [[0,0]]*(Max)

    for i in range(n):
        data = input().split()
        edge[int(data[0])] = data[1:]
        minimal = int(data[0]) if(int(data[0]) > minimal) else minimal
    #print(minimal)
    for i in range(Max):
        if(not edge[i][0] == -1):
           
            #print(i)
            for j in range( len(edge[i])):
                edge[i][j] = edge[i][j].title()
                graph[0][ dict[edge[i][j][0]]  ] = [0, 1]
       
                graph[ dict[edge[i][j][0]] ][ 27 + i ] = [edge[i][j], 1]
                graph[ 27 + i ][ Max-1 ] = [0, 1]

    #for i in range(len(graph)):
     #   print(graph[i])
    max_flow , graph , answer= fordF(0, Max-1 , Max)
    #for i in range(len(graph)):
    #   print(graph[i])
    for i in range( len(graph)):
        for j in graph[i]:
                #print(j)
                if(not j[0] == 0  and j[1] == 0):
                    pass
                    #answer.append((dict[j[0][0]], j[0]))
                    #print(dict[j[0][0]], j[0], j[1] )
                    #max_flow -= 1
    #for i in range(len(graph)):
    #   print(graph[i])
    answer.sort()
    print(max_flow)
    print("Case #%d:" %case)
    for j in range(len(answer)):
        print(answer[j])
    case += 1
