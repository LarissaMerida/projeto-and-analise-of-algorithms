people, objects, memo = [], [], []

def superSales_TD(i, cap):
	global people, objects, memo

	if(not memo[i][cap] == -1):
		return memo[i][cap]

	if(i == len(objects) or cap == 0):
		memo[i][cap] =  0
	elif(objects[i][1] > cap):
		memo[i][cap] = superSales_TD(i+1, cap)
	else:
		accept = objects[i][0] + superSales_TD(i+1, cap - objects[i][1])
		ignore  = superSales_TD(i+1, cap)
		memo[i][cap] =  accept if(accept > ignore) else ignore

	return memo[i][cap]


case = int(input())

while(case > 0):
	q_obj =int(input())
	objects,  sum , memo, people = [], 0,  [-1]*(q_obj+1), []
	#print(objects)
	for i in range(q_obj):
		objects.append([int(x) for x in input().split()])

	q_people = int(input())

	for i in range(q_people):
		people.append(int(input()))

	
	for i in range(q_obj+1):
		memo[i] = [-1]*(max(people)+1)

	for i in range(q_people):
		sum += superSales_TD(0, people[i])
	print(sum)
	case -= 1