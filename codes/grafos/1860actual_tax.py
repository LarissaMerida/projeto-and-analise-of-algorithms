data = input().split()
data = [int(x) for x in data]

for i in range(data[0]):
	tax = input().split()
	tax = [int(x) for x in tax]

#graph = [-1]*(data[0]+1)
#print(graph)
print(tax)
print(data)
'''for i in range(data[0]+1):
	graph[i] = []

for i in range(data[0]-1):
	aux = input().split()
	aux = [int(x) for x in aux]

	graph[aux[0]].append((aux[1], aux[2]))
	graph[aux[1]].append((aux[0], aux[2]))
'''
#print(graph)
