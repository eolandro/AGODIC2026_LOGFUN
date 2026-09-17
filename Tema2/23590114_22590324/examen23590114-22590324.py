#Oliver Uriel Pagola Perez 23590114
#Javier Yael Enriquez Martinez 22590324

##R001##
##20##
def fun(N):
    match N:
        case int() if N < 0:
            return None 
        case 0:
            return 1    
        case int():
            previo = fun(N - 1)
            return (previo ** N) - (2 * previo)
        case _:
            return None 

print(fun(0))
# 1
print(fun(1))
# -1
print(fun(2))
# 3
print(fun(3))
# 21
#--------------------------------------------------------------
##R002##
##25##
"""
Dada la siguiente secuencia matematica
7, 17, 37, 77, 157, 317
Encuentre la función matematica recursiva
e implementela en python
"""

def seq0(N):
    match N:
        case int() if N < 0:
            return None
        case 0:
            return 7
        case int():
            previo = seq0(N - 1)
            return (2 * previo) + 3
        case _:
            return None


print(seq0(0))
# 7
print(seq0(1))
# 17
print(seq0(2))
# 37
print(seq0(3))
# 77
#--------------------------------------------------------------

##R004##
##10##
def badaboom(Num):

    if type(Num) != int:
        return None
    match (Num % 3, Num % 5):
        case (0, 0):
            return "BadaBoom!!"
        case (0, _):
            return "Bada"
        case (_, 0):
            return "Boom!!"
        case _:
            return Num

print(badaboom(1))
# 1
print(badaboom(3))
# Bada
print(badaboom(5))
# Boom!!
print(badaboom(15))
# BadaBoom!!

#------------------------------------------------------------
##R005##
##10##
def auxiliar_badaboom(actual, limite):
    
    if actual > limite:
        return []
    
    return [badaboom(actual)] + auxiliar_badaboom(actual + 1, limite)

def lista_badaboom():
    return auxiliar_badaboom(1, 100)

L = lista_badaboom()
print(L)
#--------------------------------------------------------------
##R007##
##20##

def combinaListas(L1, L2):
    match (L1, L2):
        case ([], []):	
            return []
        case ([], _):	
            return L2
        case (_, []):	
            return L1
        case ([h1, *t1], [h2, *t2]):	#td bn
            return [h1, h2] + combinaListas(t1, t2) 
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


##R009##
##20##
def funZ(N):
    match N:
        case int() if N < 0:
            return None 
        case 0:
            return 3   
        case int():
            previo = funZ(N - 1)
            return (previo ** 3) - (3 * previo)
        case _:
            return None

# --- PRUEBAS ---
print(funZ(0))
# 3
print(funZ(1))
# 18
print(funZ(2))
# 5778
print(funZ(3))
# 192900153618

##R010##
##10##
M = [
    [9,8,7],
    [4,5,6],
    [3,2,1]
]

def impMat(matriz):
    
    match matriz:
        case []:
            return
        case [Fila, *Resto]:
            print(Fila)
            impMat(Resto)
        case _:
            return
        
impMat(M)
