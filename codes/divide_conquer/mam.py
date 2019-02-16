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

def binary_search(vector, size, element):
  start, end= 0, size

  while( start < end):
    center= (start+end)//2

    if( element > vector[center]):
      start = center+1
    else:
      end = center

  return start

def find(vector, element):
    i = binary_search(vector, len(vector), element)

    if( i < len(vector) and vector[i] == element):
      return i+1
    else:
      return -1

amount, marble, k  = [], [], 1

amount = input().split()
amount = [int(i)  for i in amount]

while(amount[0] != 0 and amount[1] != 0):
  print('CASE# %d:'%k)
  for i in range(amount[0]):
    marble.append(int(input()))
  marble = quickSort(marble)

  for i in range(amount[1]):
    element = int(input())
    result = find(marble, element)
    if(result == -1):
      print(element, 'not found')
    else:
      print(element,'found at',result)
      

  amount, marble, k = [], [], k +1
  amount = input().split()
  amount = [int(i)  for i in amount]