#23590552 Luis Carlos Cuellar Trejo
#23590567 Jose Luis Acosta Garcia
#R001##
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
def F(N):
    if type(N) != int:
        return "Valor no valido"
    if N == 0:
        return 1
    else:
        return ( F(N-1)**N ) - ( 2 * F(N-1) ) 

print(F(0))    
print(F(1))
print(F(2))
print(F(3))

#----------------------------------------------------------#
#R2
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
    if N == 0:
        return 7
    return seq0(N-1) + 10 * (2**(N-1))

print(seq0(0))  
print(seq0(1))  
print(seq0(2))  


#-------------------------------------
#R4
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
	"""
def badaboom(Num):
    if (type(Num) != int and type(Num) != float):
        return "Este no es un numero, no se puede evaluar"
    if (Num % 3 == 0 and Num % 5 == 0):
          return "Bada Boom!!"
    if (Num % 3 == 0):
          return "Bada"
    if (Num % 5 == 0):
        return "Boom!!"
    else:
        return Num
	
print(badaboom(1))

print(badaboom(3))
# Bada
print(badaboom(5))
# Boom!!
print(badaboom(15))
# BadaBoom!!


#----------------------------------------
"""""""""
#R10
"""
##R010##
##10##
"""
Defina una función recursiva que permita imprimir
una matriz, una matriz en realidad es una lista
de listas
"""

M = [
	[9,8,7],
	[4,5,6],
	[3,2,1]
]

def impMat(matriz):
    if not matriz:
        return
    match matriz:
        case [P]:
            print(P)
        case [P, *F]:
            print(P)
            impMat(F)
    
	
impMat(M)
#[9,8,7],
#[4,5,6],
#[3,2,1]

#-------------------------------
""""""
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
def Fun_Z(N):
    if type(N) != int:
        return "Valor no valido"
    if N == 0:
        return 3
    else:
        return ( Fun_Z(N-1)**3 ) - ( 3 * Fun_Z(N-1) ) 

print(Fun_Z(0))    
print(Fun_Z(1))
print(Fun_Z(2))
print(Fun_Z(3))

#---------------------------------
""""""
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

    if not L1 and not L2:
        return []

    if not L1 or not L2:
        match (L1, L2):

            case ([A, *F1], []):
                return [[A]] + combinaListas(F1, [])

            case ([], [B, *F2]):
                return [[B]] + combinaListas([], F2)

    match (L1, L2):

        case([A], [B]):
                    return [[A, B]]

        case ([A, *F1], [B, *F2]):
            return [[A, B]] + combinaListas(F1, F2)

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