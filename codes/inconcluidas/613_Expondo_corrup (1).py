
graph, visited, free, components, tam_p, tam_d = [] ,[],  100, [], 0, 0
Max , components_w, memo = 2*free, 0, {}

def dfs(u):
    global visited, graph, components, w, components_w, tam_p, tam_d
    visited[ u ] = True 
    #print("visited",u, w[u])
    components_w += w[u]
    if (u < free):
        tam_d += 1
    else:
        tam_p += 1

    for v in graph[ u ]:
        if not visited[ v ] : 
            #print("Not visited", v)
            dfs(v)
        
def mochila(i, cap, part):
    global components, memo

    if(cap < 0):
        return -10000

    if ( i == len(components)):
        return 0   

    if ( (i, cap) in memo):
        return memo[ (i, cap) ]  

    opt1 = components[i][1][ (part+1)%2 ] + mochila(i+1, cap - components[i][0], part)
    opt2 = components[i][1][part] + mochila(i+1, cap, part)

    memo[ (i,cap) ] = max(opt1, opt2)
    return memo[(i,cap)]    

data = [int(x) for x in input().split()]

graph, visited,w = [[]]*Max , [[]]*Max, [[]]*Max
for i in range(Max):
    graph[i] = []
    visited[i] = False
    w[i] = 0

d = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]


for i in range(data[0]):
    w[i] = d[i]
for i in range(data[1]):
    w[ free+ i] = p[i]

for i in range(data[2]):
    edge = [int(x) for x in input().split()]

    graph[ edge[0]-1 ].append( free + edge[1] -1  )
    graph[ free + edge[1]-1 ].append(  edge[0]-1 )

for i in range(data[0]):
    if(not visited[i]):
        dfs(i)
        components.append( (components_w, [tam_d, tam_p]) )
        components_w, tam_d, tam_p = 0, 0, 0

for i in range(data[1]):
    if(not visited[ free + i]):
        dfs( free + i )
        components.append( ( components_w, [tam_d, tam_p] ))
        components_w, tam_d, tam_p = 0, 0, 0


better_d = mochila(0, data[3], 0)
memo = {}
better_p = mochila(0, data[3], 1)
print("{} {}".format(better_d, better_p))