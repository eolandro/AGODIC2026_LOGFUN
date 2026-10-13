import random
def mod(fun):
	def mod_resul(N):
		L = fun(N)
		if random.choice([True, False]):
			L.append(-1.5)
		return L
	return mod_resul

def calcular_collatz(N):
	#...
	if N == 1:
		return [N]
	if N % 2 == 0:
		return [N] + calcular_collatz(N/2)
	else:
		return [N] + calcular_collatz((N*3) + 1)

@mod
def collatz(N):
	return calcular_collatz(N)

#...
