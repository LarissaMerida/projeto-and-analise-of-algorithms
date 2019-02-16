from math import *

def merge(left, right, size):
	j, k, c = 0, 0, []

	for i  in range(size):
		if( k == len(right) or ( j< len(left) and left[j] < right[k])):
			c.append(left[j])
			j = j + 1
		else:
			c.append(right[k])
			k = k+1
	return c

def mergeSort(vector):
	if( len(vector) <= 1):
		return vector;

	center = int(floor(len(vector)/2))
	left, right = vector[0: center], vector[center: len(vector)]

	left = mergeSort(left)
	right = mergeSort(right)
	result = merge(left, right, len(left) + len(right))
	return result


def binary_search(vector, size, element):
	start, end, aux, greaterSum = 0, size-1, -1, 100000

	while( start <= end):
		center, sum = int(floor((start+end)/2)), 0

		for i in range(center, size):
			sum += (vector[i] - vector[center])

		if( element > sum):
			end = center-1
		else:
			if( element < sum):
				start = center+1
				if( sum < greaterSum):
					aux = center
					greaterSum = sum
			else:
				return vector[center]
	return vector[aux]

amount , tree_height, result = [], [] ,  []

amount = input().split()
tree_height = input().split()

amount = [int(i) for i in amount]
tree_height = [int(i) for i in tree_height]

left = tree_height[0: int(floor(len(tree_height)/2))] 
right = tree_height[int(floor(len(tree_height)/2)): amount[0]]
tree_height = mergeSort(tree_height)

print(tree_height)
print(binary_search(tree_height, len(tree_height), amount[1]))