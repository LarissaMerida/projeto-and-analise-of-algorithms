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

def checks(vector, tam):
	cont = 0
	for i in range(len(vector)):
		cont += (vector[i]//tam)
	return cont

def binary_search(vector, size, element):
  start, end, end1, start1 = 0, size, 0, 0

  while( start < end):
    center = (start+end)//2
    if(vector[center] != 0):
    	amount = checks(vector, vector[center])

    if( element > amount):
    	start1 = start
    	start = center+1
    else:
    	end1= end
    	end = center

  return start1, end1

def binary_search_value(vector, element, sandwiches):
  start, end, better = 0, len(vector), 0

  while( start < end):
    center = int((start+end)/2)
    if(vector[center] != 0):
    	amount = checks(sandwiches, vector[center])
    
    if( element >= amount):
    	start = center+1
    else:
    	end = center

  if(vector[center] != 0):
  	amount = checks(sandwiches, start)
  if(amount == element):
  	return start
  else:
  	return start-1

amount_people = int(input())
quantify_sandwiches = int(input())

sandwiches = input().split()
sandwiches = [int(x) for x in sandwiches]
sandwiches = quickSort(sandwiches)
start, end = binary_search(sandwiches, len(sandwiches), amount_people)

aswer, cont = [0]*sandwiches[start-1], 1

for i in range(sandwiches[start-1]):
	aswer[i] = cont
	cont += 1

aswer = aswer[sandwiches[start-2] : sandwiches[start-1]]
print(binary_search_value(aswer, amount_people, sandwiches))
