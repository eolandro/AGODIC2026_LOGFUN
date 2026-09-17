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
    if N == 0:
        return 1
    return fun(N-1)**N - 2*fun(N-1)
print(fun(0))
print(fun(1))
print(fun(2))
print(fun(3))
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
def seq0(n):
    if n == 0:
        return 7
    return 2 * seq0(n-1) + 3

print("----------------")
print(seq0(0))
print(seq0(1))
print(seq0(2))
print("----------------")	
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
def impGrafCirR(grafo, inicio, limite):
    if inicio == limite:
        print(inicio)
        return
    match grafo:
        case []:
            return
        case [[A, B], *F]:
            if A == inicio:
                impGrafCirR(grafo, B, limite)
                print(inicio)
                return
            return impGrafCirR(F, inicio, limite)

print("----------------")
impGrafCirR(Grafo,"AZQ","GRX")
print("----------------")
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
    if Num % 3 == 0 and Num % 5 == 0:
        return "Bada Boom!!"
    if Num % 3 == 0:
        return "Bada"
    if Num % 5 == 0:
        return "Boom!!"
    return Num

print("----------------")
print(badaboom(1))
print(badaboom(3))
print(badaboom(5))
print(badaboom(15))
print("----------------")

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

def lista_badaboom():
    return bb(1)


def bb(n):
    if n > 100:
        return []
    if n % 15 == 0:
        return ["BadaBoom!!"] + bb(n + 1)
    if n % 3 == 0:
        return ["Bada"] + bb(n + 1)
    if n % 5 == 0:
        return ["Boom!!"] + bb(n + 1)
    return [n] + bb(n + 1)


L = lista_badaboom()
print(L)


##R009##
##20##
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
M = [
	[9,8,7],
	[4,5,6],
	[3,2,1]
]

def impMat(matriz):
    if not matriz:
        return []
    match matriz:
        case [matriz]: #cuando solo hay un elemento en la lista
            print(matriz)
            return []
        case [matriz, *F]:#mas de un elemento
            print(matriz)
            return impMat(F)
        case _:
            return[]#no era una lista
impMat(M)


##R010##
##10##
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
# 19
"""

def funz(N):
    if type(N) != int or N < 0:
        return None
    if N == 0:
        return 3
    return funz(N-1)**3 - 3*funz(N-1)

print(funz(0))
print(funz(1))
print(funz(2))
print(funz(3))