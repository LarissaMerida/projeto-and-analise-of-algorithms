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

def buscaBinaria(v, n, elem):
    inicio = 0
    final = n-1
    temp = -1
    somaMenor = 100000
    while( inicio <= final):
        meio = int((inicio+final)/2)
        soma = 0
        for i in range(meio, n):
            soma+=(v[i] - v[meio])
            
        if elem > soma:
            final = meio-1
        else:
            if elem < soma:
                inicio = meio+1
                if soma < somaMenor:
                    temp = meio
                    somaMenor = soma
            else:
                return v[meio]           
    return v[temp]


quant, alturas, result = [], [] ,  []

quant = input().split()
alturas = input().split()

quant= [int(i) for i in quant]
alturas = [int(i) for i in alturas]

alturas = quicksort(alturas)
print(buscaBinaria(alturas, quant[0], quant[1]))