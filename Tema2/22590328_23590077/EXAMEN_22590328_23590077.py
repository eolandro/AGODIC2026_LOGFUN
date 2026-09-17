# Examen realizado por 
# González Pérez David Aly y Aguilar Cervantes Angel Gabriel
# 22590328_23590077



print( "##########################  ejercicio 1 ########################")
##R001##
##20##
"""
Escriba la funcion respectiva en python
para la siguiente funcion matematica
f(0) = 1
f(n) = f(n-1)**n  - 2*f(n-1)

Demostracion
f(0) = 1
f(1) = -1
f(2) = 3
f(3) = 21

defina una funcion en python

def fun(N):
	pass
	
print(fun(0))
#1
print(fun(1))
#-1
print(fun(2))
#3
print(fun(3))
#21
"""

def fun(N):
	if type(N) != int:
		return None
	if N == 0:
		return 1
	else:
		return ((( fun ( N - 1 ) ) **N ) - ( 2 * fun ( N - 1 )))

print(fun(0))
#1
print(fun(1))
#-1
print(fun(2))
#3
print(fun(3))
#21     

print( "##########################  ejercicio 2 ########################")

##R002##
##25##
"""
Dada la siguiente secuencia matematica
7, 17, 37, 77, 157, 317
Encuentre la función matematica recursiva
e implementela en python

def seq0():
	pass
	
print(seq0(0))
#7
print(seq0(1))
#17
print(seq0(2))
#37

"""



def seq0(N):
	if type(N) != int:
		return None
	if N == 0:
		return 7
	else:
		return (2 * (seq0 (N - 1)) + 3 )


print(seq0(0))
#7
print(seq0(1))
#17
print(seq0(2))
#37
print(seq0(3))
#77
print(seq0(4))
#157
print(seq0(5))
#317




print( "##########################  ejercicio 3 ########################")
##R003##
##45##
"""
Recorrido en un grafo circular
Defina una funcion recursiva que imprima todos
los elementos de un grafo circular en orden inverso

AZQ → BXQ → CYQ → DWQ → EVQ
 ↑                       ↓
JUQ ← GRX ← HSX ← ITQ ← FUQ


Grafo = [
	["AZQ","BXQ"],
	["BXQ","CYQ"],
	["CYQ","DWQ"],
	["DWQ","EVQ"],
	["EVQ","FUQ"],
	["FUQ","GRX"],
	["GRX","HSX"],
	["HSX","ITQ"],
	["ITQ","JUQ"],
	["JUQ","AZQ"]
]


def impGrafCirR(grafo,inicio,limite):
	pass

impGradCirR(Grafo,"AZQ","EVQ")
#EVQ
#DWQ
#CYQ
#BXQ
#AZQ


impGradCirR(Grafo,"AZQ","GRX")

#GRX
#FUQ
#EVQ
#DWQ
#CYQ
#BXQ
#AZQ
"""

print( "##########################  ejercicio 4 ########################")
##R004##
##10##
"""
Bada Boom!!! Parte 1
define una funcion en python que dado un numero entero te devuelva un 
resultado segun las siguientes condiciones:
	1) Si es multiplo de 3 coloque la cadena "Bada"
	2) Si es multiplo de 5 coloque la cadena "Boom!!"
	3) Si es multiplo de 3 y 5 coloque "Bada Boom!!"
	4) El mismo numero si no cae en los casos anteriores
	
def badaboom(Num):
	pass
	
print(badaboom(1))
# 1
print(badaboom(3))
# Bada
print(badaboom(5))
# Boom!!
print(badaboom(15))
# BadaBoom!!

"""



def badaboom(Num):
	if not Num:
		return None
	match Num:
		case int():
			if Num % 3 == 0 and Num % 5 == 0:
				return "BadaBoom!!"
			if Num % 5 == 0:
				return "Boom!!"
			if Num % 3 == 0:
				return "Bada"
			return Num											
		case _:
			return None
            
      
print(badaboom(1))
# 1
print(badaboom(3))
# Bada
print(badaboom(5))
# Boom!!
print(badaboom(15))
# BadaBoom!!


print( "##########################  ejercicio 5 ########################")
##R005##
##10##
"""
Bada Boom!!! Parte 2

Define una funcion que retorne una lista con los numeros del 1 al 100
aplicando la funcion Badaboom
	
def lista_badaboom():
	pass
	
L = lista_badaboom()
print(L)
#[1,2,"Bada",4,"Boom!!","Bada",7,8,"Bada","Boom!!",11,"Bada",13,14,"BadaBoom!!"...
"""


def lista_badaboom(N):
    if N > 100:
        return []
    return [badaboom(N)] + lista_badaboom(N + 1)



L = lista_badaboom(1)
print(L)


print( "##########################  ejercicio 6  ########################")
##R006##
##25##
"""
	Un analizador logico es una herramienta para ver señales 
	electricas en un circuito o computadora
	
	Una persona se le ha dañado su laptop y no tiene acceso completo
	al sistema operativo (Pantalla de la muerte) por lo que se dispone
	a extraer el disco duro, sin embargo al conectarlo en una PC
	este esta cifrado con Bitlocker y requiere una contraseña
	
	Usando el anterior mencionado analizador logico es posible ver la
	contraseña en el momento de arranque laptop. 
	Pero el analizador logico no manda la contraseña en texto convencional
	lo manda un byte en dos listas de numeros hexadecimales de 8 
	posiciones de siguiente manera:
	
	Supongamos que se envia la contraseña '12344321' en hexamedecimal
	equivale a 0x31,0x32,0x33,0x34,0x34,0x33,0x32,0x31  y las listas 
	serian las siguientes:
	#   |1|2|3|4|4|3|2|1
	A = [3,3,3,3,3,3,3,3]
	B = [1,2,3,4,4,3,2,1]
	
	defina la funcion decodifica que nos mande la contraseña 
	original apoyate de la funcion <chr> de python que convierte un numero
	en una cadena segun su ascii
	
	print(chr(49))
	
	ejemplo:
	
	A = [3,3,3,3,3,3,3,3]
	B = [1,2,3,4,4,3,2,1]
	
	def decodifica(LA,LB):
		pass
	
	PASS = decodifica(LA,LB)
	print(PASS)
	# 12344321
"""

def combinaListas(L1,L2):
	if not L1:
		return L2
	if not L2:
		return L1
	match L1, L2:
		case [list(),list()]:
			return [L1[0], L2[0]] + combinaListas(L1[1:], L2[1:])
		case _:
			return None

def decodifica(LA, LB):
	if not LA or not LB:
		return ""
	match LA, LB:
		case [list(),list()]:
			valor = LA[0] * 16 + LB[0]
			return chr(valor) + decodifica(LA[1:], LB[1:])

A = [3, 3, 3, 3, 3, 3, 3, 3]
B = [1, 2, 3, 4, 4, 3, 2, 1]

PASS = decodifica(A, B)
print(PASS)



print( "##########################  ejercicio 7 ########################")
##R007##
##20##
"""
Una funcion toma dos listas L1 y L2, las une en una sola
combiando primer elemento de L1 con el primer elemento de L2.

Si una de las dos listas se agota simplemente une el resto de la lista a
la lista resultante


def combinaListas(L1,L2):
	pass

R = combinaListas([1,2,3],["a","b","c"])
print(R)
# [1,"a",2,"b",3,"c"]

R = combinaListas([1],["a","b","c"])
print(R)
# [1,"a","b","c"]

R = combinaListas([1,2,3],["a"])
print(R)
# [1,"a",2,3]


R = combinaListas([1,2,3],[])
print(R)
# [1,2,3]


R = combinaListas([],["a","b","c"])
print(R)
# ["a","b","c"]

"""

def combinaListas(L1,L2):
	if not L1:
		return L2
	if not L2:
		return L1
	match L1, L2:
		case [list(),list()]:
			return [L1[0], L2[0]] + combinaListas(L1[1:], L2[1:])
		case _:
			return None

		


R = combinaListas([1,2,3],["a","b","c"])
print(R)
# [1,"a",2,"b",3,"c"]

R = combinaListas([1],["a","b","c"])
print(R)
# [1,"a","b","c"]

R = combinaListas([1,2,3],["a"])
print(R)
# [1,"a",2,3]


R = combinaListas([1,2,3],[])
print(R)
# [1,2,3]


R = combinaListas([],["a","b","c"])
print(R)
# ["a","b","c"]










print( "##########################  ejercicio 8 ########################")
##R008##
##35##
"""
Procesar data

Utilizando el patron de diseño composicion recursiva obten la
salida correspondiente:

R = "29590095,ROMAY TACITURNO RENE FERNANDA,0,1,1,1,1,1,1,0"

T = composicion_recursiva(R,[fun1,fun2,fun3,funN..])
print(T)
# [29590095,"ROMAY TACITURNO RENE FERNANDA",2,6]
"""

print( "##########################  ejercicio 9 ########################")
##R009##
##20##
"""
Escriba la funcion respectiva en python
para la siguiente funcion matematica
f(0) = 3
f(n) = f(n-1)**3  - 3*f(n-1)

Demostracion
f(0) = 3
f(1) = 18
f(2) = 5778
f(3) = 192900153618

defina una funcion en python

def funZ(N):
	pass
	
print(fun(0))
# 3
print(fun(1))
# 18
print(fun(2))
# 5778
print(fun(3))
# 192900153618
"""



def funZ(N):
	if type(N) != int:
		return None
	if N == 0:
		return 3
	return ((funZ( N - 1 )) **3) - (3 * ( funZ ( N - 1 )))
		# f(n) = f(n-1)**3  - 3*f(n-1)
	
print(funZ(0))
# 3
print(funZ(1))
# 18
print(funZ(2))
# 5778
print(funZ(3))
# 192900153618

print( "##########################  ejercicio 10 ########################")
##R010##
##10##
"""
Defina una función recursiva que permita imprimir
una matriz, una matriz en realidad es una lista
de listas

M = [
	[9,8,7],
	[4,5,6],
	[3,2,1]
]

def impMat(matriz):
	pass
	
impMat(M)
#[9,8,7],
#[4,5,6],
#[3,2,1]

"""


def impMat(matriz):
    if not matriz:
        return None
    if type(matriz) == list:
        print(matriz[0])
        impMat(matriz[1:])

impMat([
	[9,8,7],
	[4,5,6],
	[3,2,1]])