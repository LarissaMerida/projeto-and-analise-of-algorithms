import sys
sys.setrecursionlimit(15000000)

memo, hastes, choices , pred = [], [], [], []

def corte_naive(n):
    global hastes
    if(n <= 0):
        return 0
    else:
        best = -1
        for  i in range(n):
            #print(hastes[i])
            best = max(best, hastes[i]+corte_naive(n-i-1))
        return best

def corte_TD(n):
    global hastes, memo

    if(not memo[n] == -1 ):
        return memo[n]

    if(n <= 0):
        return 0
    else:
        best = -1
        for i in range(n):
            best = max(best, hastes[i]+corte_TD(n-i-1))

    return best

def corte_BU(n):
    memo[0] = 0

    for i in range(1, n+1):
        best = -1

        for j in range(i):
                best = max(best, memo[j] + hastes[i-(j+1)])
        memo[i] = best
    return memo[n]

tam = int(input())
while(tam):

    hastes = [0]*(tam+1)
    for i in range(tam):
        hastes[i] = int(input())
   
    memo, pred = [-1]*(tam+1),[-1]*(tam+1)
   # print(corte_naive(tam))
    #print(corte_TD(tam))
    print(corte_BU(tam))
    tam = int(input())
