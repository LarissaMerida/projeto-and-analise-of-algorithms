import time
start_time = time.clock()
def quicksort(v):
    dir, esq, pivot_list = [], [] ,  []

    if len(v) <= 1:
        return v
    else:
        pivot = v[0]
        for i in v:
            if i < pivot:
                esq.append(i)
            elif i > pivot:
                dir.append(i)
            else:
                pivot_list.append(i)
        dir = quicksort(dir)
        esq = quicksort(esq)

    return esq + pivot_list + dir

def checks(vector, tam,  element):
  cont, possible = 0, 0

  for i in range(len(vector)):
    if(vector[i]  >= tam):
        cont += (vector[i]- tam)
    #print("Cconts",cont, vector[i], tam, vector)
  if(cont < element):
    possible = 1
 # print("eeu",cont)
  return cont

def binary_search_value(steps, start1, end1, element):
  start, end, center = start1, end1, 0
  #print(end)
  while(end - start >= 0.000019):
    center = (start+end)/2.0
    #print(center)
    possible = checks(steps, center, element)

    if(possible > element):
      #  print("a")
        start = center+0.000019

    elif(possible < element):
     # print('C', start, end, center, possible)
      end = center-0.000019
    else:
        #print("B")
        return center
  possible = checks(steps, end, element)
  #print(start, end, center, possible)
  if(abs(element - possible)  >= 0.000019  or checks(steps, end, element) == element):
    return end
  elif(abs(element - checks(steps, start, element))  >= 0.000019 or checks(steps, start, element) == element):
  	return start
  elif(abs(element - checks(steps, center, element))  >= 0.000019 or checks(steps, center, element) == element):
  	return center
  else:
    return -1
 
date = input().split()
date = [float(x) for x in date]
while(date[0] != 0 and date[1] != 0):
    strip_length = input().split()
    strip_length = [float(x) for x in strip_length]
    ##strip_length = quicksort(strip_length)
 
    if(sum(strip_length) == date[1]):
            print(":D")
    elif(sum(strip_length) < date[1]):
    	print("-.-")
    else:
        end = max(strip_length)#strip_length[int(date[0])-1]
        start = min(strip_length)
        if(start == end):
             start = 0
        #print(start, end)
        n = binary_search_value(strip_length, start, end, date[1])

        if(n == -1):
            print("-.-")
        else:
        	if(abs(date[1]  - checks(strip_length, n, date[1])) > 0.00019):
        	   m =  binary_search_value(strip_length, 0, n, date[1])
        	   print(format(m, ".4f"))
        	else:
        		print(format(n, ".4f"))

    date = input().split()
    date = [float(x) for x in date]