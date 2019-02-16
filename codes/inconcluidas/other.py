
from queue import *
Max = 10
pred, dict1 = [], {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L':12, 
                    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 
                    'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
dict2 = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L':0, 
        'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 
        'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

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
               # print(v , graph[u][v])
                dist[ v ] = int(dist[int(u)]) + 1
                vstd[ v ] = True
                pred[ v ] = u
                q.put(v)
    #print(vstd[ar])
    return 0 #(dist, vstd, u)

def fordF(source, target, tam):
    global graph
    residual_graph, max_flow = graph, 0

    while(bfs(residual_graph, tam, 0, target)):

        i , path_flow = target, 100*100
        while(not i == 0):
            u = pred[i]
            path_flow = min( path_flow, residual_graph[u][i][1]) 
            i = pred[i]

        i = target
        while(not i == source):
            u = pred[i]
            residual_graph[u][i][1] -= path_flow
            residual_graph[i][u][1] += path_flow
            #print(residual_graph[u][i])
            #if(not residual_graph[u][i][0] == 0  and residual_graph[u][i][1] == 0):
                #print(residual_graph[u][i])
            i = pred[i]
        max_flow += path_flow   


   # for i in residual_graph:
    #    print(i)
    return max_flow, residual_graph

cases = int(input())
case = 1
while(case <= cases):
    n = int(input())
    edge, minimal , graph, answer, k = [[-1]]*(Max), -1,[[0,0]]*(Max), [], 1

    for i in range(Max):
        graph[i] = [[0,0]]*(Max)

    for i in range(n):
        data = input().split()
        m = int(data[0])
        edge[ m ] = data
        minimal = int(edge[ m ][0]) if(int(edge[ m ][0]) > minimal) else minimal
        for j in range(1 , len(edge[ m ])):
            edge[ m ][j] = edge[ m ][j].title()
            if(dict2[edge[ m ][j][0]] == 0):
                dict2[edge[ m ][j][0]] = k
                k +=1
    #print(k, minimal)
    #print(edge)
    for i in range(Max):
        #print(edge[i])
        if(not edge[i][0] == -1):
           
            for j in range(1, len(edge[i])):
                edge[i][j] = edge[i][j].title()
                graph[0][ dict2[edge[i][j][0]] + minimal ] = [0, 1]
            
                graph[ dict2[edge[i][j][0]] + minimal ][ i ] = [edge[i][j], 1]
                graph[ i ][ Max-1 ] = [0, 1]
   # for i in graph:
     #   print(i)

   
    max_flow ,graph = fordF(0, Max-1 , Max)
    #print(max_flow)
   # print("AAA")
    #for i in graph:
     #   print(i)

    for i in range( len(graph)):
        for j in range(len(graph[i])):
            if(not graph[i][j][0] == 0 and max_flow >= 0) and graph[i][j][1] == 0:
                #print(graph[i][j])
                #print(graph[j][i])
                answer.append((dict1[ graph[i][j][0][0] ], graph[i][j][0]))
                #print()
                max_flow -=1
 
    answer.sort()
    #print(answer)
    #print(dict1)
    print("Case #%d:" %case)
    for j in range(len(answer)):
        print(answer[j][1])
    case += 1
