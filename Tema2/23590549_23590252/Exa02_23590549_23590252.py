import random


##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print() 
"""

concepto_closure = "##R001## \nUn closure es una función que se define dentro de otra " \
"y puede seguir usando las variables de la función externa, incluso después " \
"de que esta haya terminado. Así, la función interna conserva esos valores y los utiliza " \
"cuando es llamada. \n"
print(concepto_closure)



##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""
concepto_wrapper = "##R002## \nUn wrapper es una función que envuelve o utiliza una función general y la adapta para realizar una tarea específica. \n"
print(concepto_wrapper)


print("# R003 #")
def leyCoulomb(K, q1, q2, r):
    return (K * (q1 * q2)) / r**2

k = 9 * (10**9)

def CoulombVacio(q1, q2, r):
    return leyCoulomb(k, q1, q2, r)

def CoulombAire(q1, q2, r):
    return leyCoulomb(k / 1.00051, q1, q2, r)

def CoulombAlumina(q1, q2, r):
    return leyCoulomb(k / 5.9, q1, q2, r)

def CoulombPVC(q1, q2, r):
    return leyCoulomb(k / 3.4, q1, q2, r)

def CoulombAgua(q1, q2, r):
    return leyCoulomb(k / 81, q1, q2, r)

def CoulombGlicerina(q1, q2, r):
    return leyCoulomb(k / 43, q1, q2, r)

q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2
print(CoulombVacio(q1, q2, r))
print(CoulombAire(q1, q2, r))
print(CoulombAlumina(q1, q2, r))
print(CoulombPVC(q1, q2, r))
print(CoulombAgua(q1, q2, r))
print(CoulombGlicerina(q1, q2, r))




print("\n# R004 #")

def leyCoulomb(K, q1, q2, r):
    return (K * (q1 * q2)) / r**2

def parcialLeyCoulomb(K):
    def inferior1(q1):
        def inferior2(q2):
            def inferior3(r):
                return leyCoulomb(K, q1, q2, r) 
            return inferior3
        return inferior2
    return inferior1

k = 9 * (10**9)

F0 = parcialLeyCoulomb(k)          
F1 = F0(3 * (10**-6))             
F2 = F1(-8 * (10**-6))             
F3 = F2(2)                             
print(F3)                             



print("\n# R005 #")

def leyCoulombCurri(K):
    def inferior1(q1):
        def inferior2(q2):
            def inferior3(r):
                return (K * q1 * q2) / r**2
            return inferior3
        return inferior2
    return inferior1

k = 9 * (10**9)
q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r  = 2

F = leyCoulombCurri(k)(q1)(q2)(r)
print(F)

print("\n# R006 #")

def calcularGravedad(astro):
    def Luna(m1, m2, d):
        return (1.62 * (m1 * m2)) / d**2
    def Marte(m1, m2, d):
        return (3.711 * (m1 * m2)) / d**2
    def Ganímedes(m1, m2, d):
        return (1.42 * (m1 * m2)) / d**2
    def Encélado(m1, m2, d):
        return (0.113 * (m1 * m2)) / d**2
    def Titán(m1, m2, d):
        return (1.352 * (m1 * m2)) / d**2
    def Venus(m1, m2, d):
        return (8.87 * (m1 * m2)) / d**2

    match astro:
        case "Luna":   
            return Luna
        case "Marte":   
            return Marte
        case "Ganímedes":
            return Ganímedes
        case "Encélado": 
            return Encélado
        case "Titán":     
            return Titán
        case "Venus":   
            return Venus
        case _:         
            return lambda m1, m2, d: None  


print(calcularGravedad("Luna")(100, 130, 2))
print(calcularGravedad("Marte")(100, 130, 2))
print(calcularGravedad("Ganímedes")(100, 130, 2))
print(calcularGravedad("Encélado")(100, 130, 2))
print(calcularGravedad("Titán")(100, 130, 2))
print(calcularGravedad("Venus")(100, 130, 2))



print("\n# R0011 #")
L = [random.randint(1, 101) for N in range(100)]
S = sum(L)
print(L)
print(S)


print("\n# R0012 #")
# R012
Pares = [N for N in L if N % 2 == 0]
Impares = [N for N in L if N % 2 != 0]
print("Pares:\n", Pares)
print("Impares:\n", Impares)
