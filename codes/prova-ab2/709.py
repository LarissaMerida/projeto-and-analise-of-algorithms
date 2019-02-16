import sys
sys.setrecursionlimit(15000000)
def calBadness(i,j, length):
    global words

    if i == j:
        return 0 # cabe uma palavra exatamente de length

    amount_actual = 0
    for k in range(i, j+1):
        amount_actual += len(words[k]) #espaco usando agora
   
    remaining_size  = ( length - amount_actual ) %  (j - i )
    standard_split = ( length - amount_actual) // (j - i )
    q =  j - i - remaining_size
    amount_space =  q*( standard_split - 1)**2 + ( standard_split**2)*remaining_size
    return  amount_space
    #retorna a quantidade de espacos usado com espaço normal + a quantidade de espacos usado com divisão padrão

def badnessFill(length):
    global badness, words

    for i in range(len(words)):
        for j in range(i, len(words) ):
            if badness[i][j] < 0:  # passou do limite
                badness[i][j] = 100**100
            elif i == j and len(words[j]) < length:
                badness[i][j] = 500
                # cabe uma palavra 
            else:
                badness[i][j] = calBadness(i, j, length)
                #print(badness[i][j], i, j)

def dpFunction():   
    global words, dp, badness, parent_pointer
    value , dp[ len(words) ] = 0, 0

    for i in range(len(words)-1,  -1, -1):
        minimal = 100**100
        for j in range(len(words), i, -1):
            value = dp[j] + badness[i][j-1]
            if value < minimal:
                minimal = value
                parent_pointer[i] = j
        dp[i] = minimal

def output(length, i, j):
    global words
    actualLenght, q = 0, j - i-1
 
    if(i < len(words)):
        #print( words[i], end = "1\n")
        for k in range(i, j):
            actualLenght += len(words[k])
        if(q > 0):
            space = ( length - actualLenght )//q
            remaining_tam = (length - actualLenght )%q
        else:
            space = 0
            remaining_tam  = 0

        for k in range(i, j):
            if not k == j-1:
                print(words[k], end = "")
                for l in range(space):
                    print(" ", end = "")
               
                if 0 < (j -1 - k) <= remaining_tam:
                    print(" ", end = "")
            else:
                print(words[k], end = "")
        print("", end = "\n")
        i = j
        j = parent_pointer[i]
        output(length, i, j )

n = int(input())
while not n == 0:
    words = []
    data = input().split()
    while not data == []:
        for i in data:
            words.append(i)
        data = input().split()
    #print(words)
    badness, dp , parent_pointer = [[0]]*(len(words)+1), [], []
    for i in range(len(words)+1):
        badness[i] = [0]*(len(words))
        dp.append(-1) 
        parent_pointer.append(-1)

    for i in range(len(words)):
        badness[i][i] = n - len(words[i])  # o custo de colocar uma palavra apenas
        for j in range(i+1, len(words)):
            badness[i][j] = badness[i][j-1] - len(words[j]) - 1
            #custo da palavra anteriores + nova palavra +  espaço padrão
    
    badnessFill(n) # melhora a badness 
    dpFunction()
    
    print(dp)
    print(parent_pointer)
    output(n, 0, parent_pointer[0])
    print()
    n = int(input())