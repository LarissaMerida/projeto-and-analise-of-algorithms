def binary_search(vector, size, element):
  start, end, end1, start1 = 0, size, 0, 0

  while( start < end):
    center = (start+end)//2

    if( element > vector[center]):
    	start1 = start
    	start = center+1
    else:
    	end1= end
    	end = center

  #print(end, start, end1, start1)
  return start-1, end


tam1 = int(input())
height = [int(x) for x in input().split()]
tam2 = int(input())
monkey = [int(x) for x in input().split()]

for i in monkey:
  if(i <= height[ tam1-1 ]):
    start, end = binary_search(height, tam1, i)
    end = end if(end < tam1) else tam1-1
    #print(start, i, end)
    #print(end)
    while(end < tam1 and height[ end ] == i):
      end = end+1 
   # print(height[end], end)
    if(end < tam1 and start >= 0):
      print(height[start] , height[ end ])
    elif(end < tam1 and start < 0):
      print("X" , height[ end ])
    else:
      #print("AAAA")
      print( height[ start ], "X")
  else:
    print( height[ tam1-1 ], "X")