program , memo, best = [], [], -1

def corte_naive(i, nivel, j):
    global program, memo, best

    if(i > data[0] or j > data[1]):
        return 0
    else:
        ''''
        print(l)
        print("B", best)
        best = (best, program[i][l] + corte_naive(i-1, l, l ) )
        '''    
        for j in range(len(program[i])):
           
            #print("C", best)
            
            if(j == nivel):
                m = corte_naive(i+1, j )
                n = corte_naive(i+1, j)
                print("AAA", j, m, program[i][j] , i )
                best = max(best, program[i][j] + m )



        print(best, i)
    return best


data = [int(x) for x in input().split()]
program, cont = [[]]*(data[1]), 1

for i in range(data[1]):
    program[i] = [[]]*(data[0])

print(program)
for i in range(data[1]):
    for j in range(data[0]):
        data1 = [int(x) for x in input().split()]
        program[i][j] = data1[0]*data1[1] 

memo = [0]*(data[1])
for i in range(data[1]):
    memo[i] = [0]*(data[0])

print(memo)

print(corte_naive(0, 0))