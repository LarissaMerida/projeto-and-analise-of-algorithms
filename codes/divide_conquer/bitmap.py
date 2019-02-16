def checks(matrix, iniL, iniC, fimL, fimC, quant):
	a = '2'
	for i in range(iniL, fimL):
		for j in range(iniC, fimC):
			if(matrix[i][j] == '0' and (a == '0' or a == '2')):
				a = '0'
			elif( matrix[i][j] == '1' and (a == '1' or a == '2')):
				a = '1'
			else:
				return 'D'
	return a

def bitmap(matrix, lin1, col1, lin2, col2, quant):
	if(lin1 == lin2 or col1 == col2):
		return
	d = checks(matrix, lin1, col1, lin2, col2, quant)
	if d == 'D':
		if(quant == 50):
			print()
			quant = 0
		print("D", end = '')
		quant+=1
		if(lin2 - lin1 == 1 and col2 - col1 == 1):
			return
		meioC, meioL = int((col1 + col2)/2), int((lin1 + lin2)/2)
		i, j = (lin2 - lin1)%2, (col2 - col1)%2

		bitmap(matrix, lin1, col1, meioL+i, meioC+j, quant)
		bitmap(matrix, lin1, meioC+j, meioL+i, col2, quant)
		bitmap(matrix, meioL+i, col1, lin2, meioC+j, quant)
		bitmap(matrix, meioL+i, meioC+j, lin2, col2, quant)
	else:
		if(quant == 50):
			print()
			quant = 0
		print(d, end = '')
		quant+=1
		return


case = int(input())
while(case > 0):
	info, matrix, lin, quant = [], [], [], 0

	info = input().split()
	info = [int(i) for i in info]
	for i in range(info[0]):
		lin = input()
		matrix.append(lin)

	bitmap(matrix, 0, 0, info[0], info[1], quant)
	print()

	case-=1


