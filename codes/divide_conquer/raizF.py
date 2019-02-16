def raiz(n, i, f, fim):
	meio = (i+f)/2.0

	if i-0.0009 >= fim or i > f:
		return meio
	if meio*meio == n:
		return meio
	if meio*meio > n:
		return raiz(n, i, meio-0.0009, fim)
	if meio*meio < n:
		return raiz( n, meio+0.0009, fim, fim)

n = float(input())
print(round(raiz(n, 1, n, n), 3))