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
	match N:
		case 0:	
			return 1
		case _:
			return fun(N-1)**N - 2*fun(N-1)
print("Reactivo R001")

print(fun(0))
# 1

print(fun(1))
# -1

print(fun(2))
# 3

print(fun(3))
# 21
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

la funcion matematica de la secuencia es
a(0) = 7
a(n) = 2a(n-1)+3

o aplicado al problema
a(1)= 2 * 7 + 3 = 14 + 3 = 10
          ^
          a(1-1)= a(0) = 7
"""

def seq0(n):
    if n == 0:
        return 7
    return 2 * seq0(n-1)+3
print("Reactivo R002")
print(seq0(0))
print(seq0(1))
print(seq0(2))

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

def impGradCirR(grafo, inicio, limite):
    if not grafo:
        return
    match grafo:
        case [P,*F]:
            if P[0] == inicio:
                if P[0]== limite:
                    print (limite)
                else:
                    impGradCirR(F,P[1],limite)
                    print (P[0])
            else:
                impGradCirR(F,inicio,limite)

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
print("Reactivo R003")
impGradCirR(Grafo,"AZQ","EVQ")
impGradCirR(Grafo,"BXQ","GRX")

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
	if Num % 3 == 0:
		return "Bada!!"
	if Num % 5 == 0:
		return "Boom!!"
	if Num % 3 == 0 and Num % 5 == 0:
		return "Bada Boom"

	return Num
print("Reactivo R004")

print(badaboom(1))
# 1

print(badaboom(3))
# Bada

print(badaboom(5))
# Boom!!

print(badaboom(15))
# Bada Boom!!

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
def Lista_badaboom(Lista):
	#return Lista_badaboom(list(range(1,101)))
	if not Lista:
		return []
	match Lista:
		case [P]:
			if P % 3 == 0:
				return ["Bada!!"] 
			if P % 5 == 0:
				return ["Boom!!"] 
			if P % 3 == 0 and P % 5 == 0:
				return ["Bada Boom!!"] 
			return [P]
		case [P, *F]:
			if P % 3 == 0:
				return ["Bada!!"] + Lista_badaboom(F)
			if P % 5 == 0:
				return ["Boom!!"] + Lista_badaboom(F)
			if P % 3 == 0 and P % 5 == 0:
				return ["Bada Boom" ] + Lista_badaboom(F)
			return [P] + Lista_badaboom(F)
		case _:
			return[]
print("Reactivo R005")

Lista = Lista_badaboom(list(range(1,101)))
print(Lista)

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
    if N == 0:
        return 3
    return funZ(N-1)**3  - 3*funZ(N-1)
print("Reactivo R009")

print(funZ(3))

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
def impMat(M):
	if not M:
		return
	match M:
		case [P]:
			if not P:
				return
			print(P)

		case [P,*F]:
			if not P:
				return
			if not F:
				return
			print(P)
			impMat(F)

		case _:
			return


M = [
	[9,8,7],
	[4,5,6],
	[3,2,1]
]
print("Reactivo R010")

impMat(M)

