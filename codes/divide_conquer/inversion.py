from math import *

cont = 0
def merge(left, right, size):
	global cont
	j, k, c = 0, 0, []

	for i  in range(size):
		if( k == len(right) or ( j< len(left) and left[j] <= right[k])):
			c.append(left[j])
			j = j + 1
		else:
			c.append(right[k])
			k = k+1
			cont += (len(left) - j)
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


numbers, i, j = [], 0, 1
amount_test = int(input())

while(amount_test > 0):
	input()
	amount_numbers = int(input())
	for i in range(amount_numbers):
		numbers.append(int(input()))

	numbers = mergeSort(numbers)

	print(cont)
	amount_test , numbers, cont = amount_test - 1, [], 0
