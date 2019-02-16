people, objects = [], []

def superSales_TD(i, cap):
	global people, objects

	pass

case = int(input())

while(case > 0):
	q_obj =int(input())
	objects = []
	#print(objects)
	for i in range(q_obj):
		objects.append([int(x) for x in input().split()])
	print(objects)
	q_people = int(input())
	people = []
	for i in range(q_people):
		people = int(input())

		memo = [-1]*(q_obj+1)
		for i in range(q_obj+1):
			memo[i] = [-1]*(people+1)
		prints
	case -= 1