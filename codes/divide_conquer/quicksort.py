def quickSort(vector):
	left, right, pivot_list = [], [], []

	if(len(vector) <= 1):
		return vector
	else:
		pivot = vector[ len(vector)-1 ]
		print(pivot)
		for i in vector:
			if( i < pivot):
				left.append(i)
			elif(i > pivot):
				right.append(i)
			else:
				pivot_list.append(i)

		print(right, pivot_list)
		print(left)
		right = quickSort(right)
		left = quickSort(left)

	return left + pivot_list + right


data = [int(x) for x in input().split()]
print("Estado inicial: ", end = "")
for i in range(len(data)):
	if(i < len(data)-1):
		print(data[i] , end = " | ")
	else:
		print(data[i])
data = quickSort(data)