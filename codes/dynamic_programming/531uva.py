text1, text2, memo, dim, answer = [],  [], [], [], []

def compromise_TD(i, j):
    global text1, text2, memo, dim
    if(not memo[i][j] == -1):
        return memo[i][j]

    if(i == 0 or j == 0):
        memo[i][j] = 0
    elif(text1[i-1] == text2[j-1]):
        dim[i][j] = 'D'
        memo[i][j] = 1 + compromise_TD(i-1, j-1)  
    else:
        m = compromise_TD(i, j-1)
        n = compromise_TD(i-1, j)
        if(m < n):
            memo[i][j] = n
            dim[i][j] = 'U'
        else:
            memo[i][j] = m
            dim[i][j] = 'L'

    return memo[i][j]

def compromise_BU(i, j):
    global text1, text2, memo, dim

    for k in range(i):
        memo[k][0] = 0

    for k in range(j):
        memo[0][k] = 0

    for k in range(1, i+1):
        for l in range(1, j+1):
            if(text1[k-1] == text2[l-1]):
                memo[k][l] = 1 + memo[k-1][l-1]
                dim[k][l] = 'D'
            else:
                if(memo[k-1][l] > memo[k][l-1]):
                    memo[k][l] = memo[k-1][l]
                    dim[k][l] = 'U'
                else:
                    memo[k][l] = memo[k][l-1]
                    dim[k][l] = 'L'

    return memo[i][j]

def show(i, j):
    global text1, dim, answer
    if(i == 0 or j == 0):
        return

    if(dim[i][j] == 'D'):
        show(i-1, j-1)
        answer.append(text1[i-1])
    elif(dim[i][j] == 'U'):
       show(i-1,j)
    else:
        show(i,j-1)


text1, text2 = [], []
exception = 1
while(exception):

    try:    
        data = input().split()
        while(not data[0] == '#'):
            for i in data:
                text1.append(i)
            data = input().split()

        data = input().split()
        while not data[0] == '#':
            for i in data:
                text2.append(i)
            data = input().split()

        memo, dim = [-1]*(len(text1)+1),[-1]*(len(text1)+1)
        for i in range(len(text1)+1):
            memo[i] = [-1]*(len(text2)+1)
            dim[i] = [-1]*(len(text2)+1)
    
        #print(len(text1), len(text2))
        #compromise_TD(len(text1), len(text2))
        compromise_TD(len(text1), len(text2))
        show(len(text1), len(text2))
        for i in range(len(answer)):
            
            if(i < len(answer)-1):
                print(answer[i], end=" " )
            else:
                print( answer[i])
            
        text1, text2, answer = [], [], []
    except Exception:
        exception = 0
