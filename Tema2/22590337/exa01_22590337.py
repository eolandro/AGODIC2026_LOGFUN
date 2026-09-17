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
        case int() if N == 0:
            return 1
        case int() if N > 0:
            anterior = fun(N - 1)
            return anterior ** N - 2 * anterior
        case _:
            return None


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
    match N:
        case int() if N == 0:
            return 7
        case int() if N > 0:
            return 2 * seq0(N - 1) + 3
        case _:
            return None


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
def buscar_siguiente(grafo, nodo):
    match grafo:
        case []:
            return None
        case [[origen, destino], *resto]:
            if origen == nodo:
                return destino
            return buscar_siguiente(resto, nodo)
        case _:
            return None


def pertenece(elemento, L):
    match L:
        case []:
            return False
        case [P, *F]:
            if P == elemento:
                return True
            return pertenece(elemento, F)


def recorrido_inverso(grafo, actual, limite, visitados):
    if actual == limite:
        print(actual)
        return True
    if pertenece(actual, visitados):
        return False
    siguiente = buscar_siguiente(grafo, actual)
    if siguiente is None:
        return False
    encontrado = recorrido_inverso(grafo, siguiente, limite, visitados + [actual])
    if encontrado:
        print(actual)
    return encontrado


def impGrafCirR(grafo, inicio, limite):
    match grafo:
        case []:
            return
        case [*_]:
            recorrido_inverso(grafo, inicio, limite, [])
        case _:
            return


Grafo = [
    ["AZQ", "BXQ"],
    ["BXQ", "CYQ"],
    ["CYQ", "DWQ"],
    ["DWQ", "EVQ"],
    ["EVQ", "FUQ"],
    ["FUQ", "GRX"],
    ["GRX", "HSX"],
    ["HSX", "ITQ"],
    ["ITQ", "JUQ"],
    ["JUQ", "AZQ"]
]


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
    match Num:
        case int() if Num % 3 == 0 and Num % 5 == 0:
            return "BadaBoom!!"
        case int() if Num % 3 == 0:
            return "Bada"
        case int() if Num % 5 == 0:
            return "Boom!!"
        case int():
            return Num
        case _:
            return None


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
def lista_badaboom(N=100):
    if N <= 0:
        return []
    return lista_badaboom(N - 1) + [badaboom(N)]


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
def decodifica(LA, LB):
    if len(LA) != len(LB):
        return None
    match (LA, LB):
        case ([], []):
            return ""
        case ([A, *RA], [B, *RB]):
            return chr(A * 16 + B) + decodifica(RA, RB)
        case _:
            return None


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
def combinaListas(L1, L2):
    match (L1, L2):
        case ([], _):
            return L2
        case (_, []):
            return L1
        case ([P1, *R1], [P2, *R2]):
            return [P1, P2] + combinaListas(R1, R2)
        case _:
            return None


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
def composicion_recursiva(Valor, ListaFunciones):
    match ListaFunciones:
        case []:
            return Valor
        case [PF]:
            return PF(Valor)
        case [PF, *FF]:
            return composicion_recursiva(PF(Valor), FF)
        case _:
            return None


def a_enteros(L):
    match L:
        case []:
            return []
        case [P, *F]:
            return [int(P)] + a_enteros(F)


def contar(L, valor):
    match L:
        case []:
            return 0
        case [P, *F]:
            if P == valor:
                return 1 + contar(F, valor)
            return contar(F, valor)


def separar(cadena):
    return cadena.split(",")


def convertir_matricula(L):
    M, *F = L
    return [int(M)] + F


def agrupar_valores(L):
    M, N, *V = L
    return [M, N, a_enteros(V)]


def resumir(L):
    M, N, V = L
    return [M, N, contar(V, 0), contar(V, 1)]


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
    match N:
        case int() if N == 0:
            return 3
        case int() if N > 0:
            anterior = funZ(N - 1)
            return anterior ** 3 - 3 * anterior
        case _:
            return None


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
def unir(L):
    match L:
        case []:
            return ""
        case [P]:
            return str(P)
        case [P, *F]:
            return str(P) + "," + unir(F)


def impMat(matriz):
    match matriz:
        case []:
            return
        case [P, *F]:
            separador = "," if F else ""
            print("[" + unir(P) + "]" + separador)
            impMat(F)
        case _:
            return


M = [
    [9, 8, 7],
    [4, 5, 6],
    [3, 2, 1]
]


if __name__ == "__main__":
    print(fun(0))
    print(fun(1))
    print(fun(2))
    print(fun(3))

    print(seq0(0))
    print(seq0(1))
    print(seq0(2))

    impGrafCirR(Grafo, "AZQ", "EVQ")
    impGrafCirR(Grafo, "AZQ", "GRX")

    print(badaboom(1))
    print(badaboom(3))
    print(badaboom(5))
    print(badaboom(15))

    L = lista_badaboom()
    print(L)

    LA = [3, 3, 3, 3, 3, 3, 3, 3]
    LB = [1, 2, 3, 4, 4, 3, 2, 1]
    PASS = decodifica(LA, LB)
    print(PASS)

    print(combinaListas([1, 2, 3], ["a", "b", "c"]))
    print(combinaListas([1], ["a", "b", "c"]))
    print(combinaListas([1, 2, 3], ["a"]))
    print(combinaListas([1, 2, 3], []))
    print(combinaListas([], ["a", "b", "c"]))

    R = "29590095,ROMAY TACITURNO RENE FERNANDA,0,1,1,1,1,1,1,0"
    T = composicion_recursiva(R, [
        separar,
        convertir_matricula,
        agrupar_valores,
        resumir
    ])
    print(T)

    print(funZ(0))
    print(funZ(1))
    print(funZ(2))
    print(funZ(3))

    impMat(M)
