from math import *

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


amount, marble, k  = [], [], 1

amount = input().split()
amount = [int(i)  for i in amount]

while(amount[0] != 0 and amount[1] != 0):
	print('CASE#',k)
	k +=1
	for i in range(amount[0]):
		marble.append(int(input()))
	marble = quickSort(marble)
	#print(marble)

	a = 0
	for i in range(amount[1]):
		element = int(input())
		for j in range(amount[0]):
			if( element == marble[j]):
				print(element,'found at',j+1)
				break;
			else:
				a+=1
		if(a == amount[0]):
			print(element, 'not found')

	amount, marble = [], []
	amount = input().split()
	amount = [int(i)  for i in amount]