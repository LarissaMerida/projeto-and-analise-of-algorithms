from queue import *
DEBUG = False
graph, visited, exist = [], [], 0

def dfs(u):
    global visited, graph, exist

    if (DEBUG):
        print("V", u)

    visited[ u] = True
    for v in graph[ u ]:
    	if(v == -1):
    		exist = 1
    	if not visited[ v ]:
    		exist = 1
    		dfs(v)
    return exist

def check(field, y, x, tam, graph):
	exist = 0
	if(x > 0 and field[y][x-1]== '1'):
		graph[tam*y+x].append(tam*y+ x-1)
		exist = 1

	if(x < tam-1 and field[y][x+1] == '1'):
		graph[tam*y+x].append(tam*y+x+1)
		exist = 1

	if(y > 0 and field[y-1][x] == '1'):
		graph[tam*y+x].append(tam*(y-1)+x)
		exist = 1

	if(y < tam-1 and field[y+1][x] == '1'):
		graph[tam*y+x].append(tam*(y+1)+x)
		exist = 1

	if(x > 0 and y > 0 and field[y-1][x-1] == '1'):
		graph[tam*y+x].append(tam*(y-1)+(x-1))
		exist = 1

	if(x < tam-1 and y < tam-1 and field[y+1][x+1] == '1'):
		graph[tam*y+x].append(tam*(y+1)+(x+1))
		exist = 1
	if(y < tam-1 and x > 0 and field[y+1][x-1] == '1'):
		graph[tam*y+x].append(tam*(y+1)+(x-1))
		exist = 1
	if(x < tam-1 and y > 0 and field[y-1][x+1] == '1'):
		graph[tam*y+x].append(tam*(y-1)+(x+1))
		exist = 1
	if(exist == 0):
		graph[tam*y+x].append(-1)

	return graph

case, stop = 1, 0
while(stop != 1):
	try: 
		tam = int(input())
		field , graph = [], [[]]*((tam)*(tam)+1)

		for i in range(tam):
			line =input()
			field.append(line)

		for i in range((tam)*(tam)+1):
			graph[i] = []

		for i in range(tam):
			for j in range(tam):
				#print( field[i][j], i, j)
				if( field[i][j] == '1'):
					graph = check(field, i, j, tam, graph)

		vertices, cont = (tam)*(tam)+1, 0
		visited = [False] *(vertices)

		for i in range(vertices):
			exist = 0
			if(visited[i] == False):
				exist = dfs(i)
				if(exist == 1):
					cont += 1
				#print("visited", i, cont, exist)
		print("Image number %d contains" %case, "%d war eagles."%cont)
		case += 1
	except Exception:
		stop = 1
