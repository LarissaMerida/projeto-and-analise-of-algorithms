import queue
graph, vstd, edges, tree, data = {}, {},[], {}, []

def prim():
    global graph, vstd, edges, tree, data

    if len(graph) == 0 :    
        return
    tam = data[0]
    for i in graph:
        if(len(graph[i]) > 0):
            tam = i
        tree [i]= {}

    vstd[tam] = True
    q = queue.PriorityQueue()
    
    for i in graph[tam]:
        q.put( ( graph[tam][i] , i, tam ) )

    cost = 0
    while not q.empty() :
        e = q.get()
        if e[1] in vstd : continue
        vstd[ e[1] ] , cost = True, cost + e[0]

        edges.append( (e[1],e[2]) )
        tree[ e[1] ][ e[2] ] = e[0]
        tree[ e[2] ][ e[1] ] = e[0]

        for v in graph[ e[1] ]:
            if v not in vstd:
                q.put( (graph[ e[1] ][v] , v , e[1] ) )

    return cost , tree , edges, tam

def quickSort(vector):
    left, right, pivot_list = [], [], []

    if(len(vector) <= 1):
        return vector
    else:
        pivot = vector[0]
        for i in vector:
            if( i < pivot):
                left.append(i)
            elif(i > pivot):
                right.append(i)
            else:
                pivot_list.append(i)

        right = quickSort(right)
        left = quickSort(left)

    return left + pivot_list + right

def dfs( u , id , neighbors ):
    global tree, vstd

    vstd[u] = id
    neighbors[id].append(u)
    for v in tree[u] : 
        if (tree[u][v] >= 0) and v not in vstd:
            #print("V", v, tree[u][v])
            dfs( v , id , neighbors )


data = [int(x) for x in input().split()]
for i in range(data[0]+1):
    graph[i] = {}

for i in range(data[1]):
    edge = [int(x) for x in input().split()]
    graph[edge[0]][edge[1]] =  edge[2]
    graph[edge[1]][edge[0]] = edge[2]

cost1, tree, edges, tam = prim()
print("First Spanning Tree Cost:" , cost1)

vstd, cost2 = {}, 1048584
edges = quickSort(edges)
for i in edges:
    w = graph[i[0]][i[1]]
    tree[i[0]][i[1]] = tree[i[1]][i[0]] = -1

    neighbors, vstd = [[]], {}
    dfs(  i[0] , 0 , neighbors)
    neighbors.append([])
    dfs(  i[1] , 1 , neighbors)

    for u in neighbors[0]:
        for v in neighbors[1]:
            if u in graph[v]:
                if (graph[u][v] >= 0) and (graph[u][v] - w) > 0:
                    cost2 = min( graph[u][v] - w , cost2 )

    tree[i[0]][i[1]] = tree[i[1]][i[0]] = w

print("Second Spanning Tree Cost:", cost1 + cost2)