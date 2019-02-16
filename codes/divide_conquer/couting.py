def coutingSort(list, max):
	aux, num , i= [0]*(max+1), 0, 0

	for j in range(len(list)):
		aux[list[j]] += 1
	
	while(i < len(list)):
		while(aux[num] > 0):
			list[i] = num
			aux[num], i =  aux[num] - 1, i + 1
			if(i > len(list)):
				break
		num += 1
	return list

def inversionCount(list):
	cont = 0

	for i in range(len(list)):
		for j in range(len(list)):
			if(list[i] > list[j]):
				print(list[i] , list[j])
				aux = list[i]
				list[i] = list[j]
				list[j] = aux
				cont += 1

	return cont, list

case = int(input())
while(case > 0):
	list, max, result = [], 0, []

	input( )
	amount = int(input())
	for i in range(amount):
		list.append(int(input()))

	result, list = inversionCount(list)
	print(list, result)
	case -= 1
	
