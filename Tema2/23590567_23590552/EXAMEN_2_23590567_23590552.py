##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print() 
"""
print("-"*150)
print("Pregunta 001")
print("#15#")
print("Respuesta:")
print("-"*150)
R_001 = ["Es un tipo de funcion que construye otras funciones, retorna SIEMPRE metodos o funciones como resultado en funcion de los parametros iniciales si no retorna una funcion, solo es una funcion de orden superior"]
print(R_001)
##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""
print("-"*150)
print("Pregunta 002")
print("#15#")
print("Respuesta:")
print("-"*150)
R_002 = ["Caso o funcion especializada o especifica de otra mas grande tienen poco cuerpo de funcion, compara y define parametros"]
print(R_002)
##R003##
##30##
print("-"*150)
print("Pregunta 003")
print("#30#")
print("Respuesta:")
print("-"*150)
"""
Ley de Coulomb
	
F = (K*(q1 * q2)) /r**2

k = 9 * (10**9) ((N m²) / C)

Valores de K en diferentes medios

Vacio ==> K = k
Aire  ==> K = k / 1.00051
Alumnina (Al2O3)  ==> K = k / 5.9
PVC  ==> K = k / 3.4
Agua  ==> K = k / 81
Glicerina  ==> K = k / 43

--Elabora 6 wrappers de la Ley de Coulomb para calcular la fuerza, 
entre dos cargas en una distancia determinada, correspondientes a los 6
medios diferentes presentados anteriormente.
Compruebe los wrappers considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
k = 9 * (10**9)

def coulomb(q1, q2, r, Funcion):
    K = Funcion(k)
    return (K * (q1 * q2)) / r**2

def coulombvacio(q1, q2, r):
    return coulomb(q1, q2, r, lambda k: k)

def coulombaire(q1, q2, r):
    return coulomb(q1, q2, r, lambda k: k / 1.00051)

def coulombalumina(q1, q2, r):
    return coulomb(q1, q2, r, lambda k: k / 5.9)

def coulombpvc(q1, q2, r):
    return coulomb(q1, q2, r, lambda k: k / 3.4)

def coulombagua(q1, q2, r):
    return coulomb(q1, q2, r, lambda k: k / 81)

def coulombglicerina(q1, q2, r):
    return coulomb(q1, q2, r, lambda k: k / 43)

q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

print("Vacio:     ", coulombvacio(q1, q2, r))
print("Aire:      ", coulombaire(q1, q2, r))
print("Alumina:   ", coulombalumina(q1, q2, r))
print("PVC:       ", coulombpvc(q1, q2, r))
print("Agua:      ", coulombagua(q1, q2, r))
print("Glicerina: ", coulombglicerina(q1, q2, r))
##R004##
##20##
print("-"*150)
print("Pregunta 004")
print("#20#")
print("Respuesta:")
print("-"*150)
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
k = 9 * (10**9)

def coulomb(q1, q2, r, Funcion):
    K = Funcion(k)
    return (K * (q1 * q2)) / r**2

def pcoulomb(q1):
    def inferior1(q2):
        def inferior2(r):
            def inferior3(Funcion):
                return coulomb(q1, q2, r, Funcion)
            return inferior3
        return inferior2
    return inferior1

q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2
F = pcoulomb(q1)(q2)(r)

print("Vacio:     ", F(lambda k: k))
print("Aire:      ", F(lambda k: k / 1.00051))
print("Alumina:   ", F(lambda k: k / 5.9))
print("PVC:       ", F(lambda k: k / 3.4))
print("Agua:      ", F(lambda k: k / 81))
print("Glicerina: ", F(lambda k: k / 43))
##R005##
##20##
print("-"*150)
print("Pregunta 005")
print("#20#")
print("Respuesta:")
print("-"*150)

k = 9 * (10**9)

def ccoulomb(q1):
    def inferior1(q2):
        q1q2 = q1 * q2
        def inferior2(r):
            r_2 = r**2
            def inferior3(Funcion):
                K = Funcion(k)
                return (K * q1q2) / r_2
            return inferior3
        return inferior2
    return inferior1
q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2
R0 = ccoulomb(q1)(q2)(r)(lambda k: k)
print("Vacio:     ", R0)
F = ccoulomb(q1)(q2)(r)

print("Aire:      ", F(lambda k: k / 1.00051))
print("Alumina:   ", F(lambda k: k / 5.9))
print("PVC:       ", F(lambda k: k / 3.4))
print("Agua:      ", F(lambda k: k / 81))
print("Glicerina: ", F(lambda k: k / 43))
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
##R006##
##30##
print("-"*150)
print("Pregunta 006")
print("#30#")
print("Respuesta:")
print("-"*150)
"""
Ley de la Gravitacion universal

F = (G*(m1*m2)) / d**2

Aceleracion por Gravedad en diferentes lugares del sistema solar

Luna 1.62 m/s²
Marte 3.711 m/s²
Ganímedes (Satelite de jupiter) 1.42 m/s²
Encélado 0.113 m/s²
Titan 1.352 m/s²
Venus 8.87 m/s²

Elabora un closure que dependiendo el nombre de astro, te retorne
la funcion con la gravedad adecuada

Comprueba cada caso del closure en los 6 astros considerando dos 
masas de 100kg y 130kg a 2 metros de distancia


"""

G = 6.674 * (10**-11)

def calcular_Gravedad(Astro):
    def Luna(m1, m2, d):
        g = 1.62
        return (G * ( m1 * m2 ) ) / d**2, m1 * g, m2 * g
    def Marte(m1, m2, d):
        g = 3.711
        return (G * ( m1 * m2 ) ) / d**2, m1 * g, m2 * g
    def Ganimedes(m1, m2, d):
        g = 1.42
        return (G * ( m1 * m2 ) ) / d**2, m1 * g, m2 * g
    def Encelado(m1, m2, d):
        g = 0.113
        return (G * ( m1 * m2 ) ) / d**2, m1 * g, m2 * g
    def Titan(m1, m2, d):
        g = 1.352
        return (G * ( m1 * m2 ) ) / d**2, m1 * g, m2 * g
    def Venus(m1, m2, d):
        g = 8.87
        return (G * ( m1 * m2 ) ) / d**2, m1 * g, m2 * g
    match Astro:
        case "Luna":
            return Luna
        case "Marte":
            return Marte
        case "Ganímedes":
            return Ganimedes
        case "Encélado":
            return Encelado
        case "Titan":
            return Titan
        case "Venus":
            return Venus
        case _:
            return lambda m1, m2, d: ((G * (m1 * m2)) / d**2, 0, 0)

m1 = 100
m2 = 130
d = 2

print("Luna:     ", calcular_Gravedad("Luna")(m1, m2, d))
print("Marte:    ", calcular_Gravedad("Marte")(m1, m2, d))
print("Ganímedes:", calcular_Gravedad("Ganímedes")(m1, m2, d))
print("Encélado: ", calcular_Gravedad("Encélado")(m1, m2, d))
print("Titan:    ", calcular_Gravedad("Titan")(m1, m2, d))
print("Venus:    ", calcular_Gravedad("Venus")(m1, m2, d))
print("Otro:     ", calcular_Gravedad("Pluton")(m1, m2, d))
##R007##
##20##
print("-"*150)
print("Pregunta 007")
print("#20#")
print("Respuesta:")
print("-"*150)
"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
G = 6.674 * (10**-11)
def gravitacion(m1, m2, d):
    return (G * (m1 * m2)) / d**2

def pgravitacion(m1):
    def inferior1(m2):
        def inferior2(d):
            return gravitacion(m1, m2, d)
        return inferior2
    return inferior1
m1 = 100
m2 = 130
d = 2
F = pgravitacion(m1)(m2)
print(F(2))
##R008##
##20##
print("-"*150)
print("Pregunta 008")
print("#20#")
print("Respuesta:")
print("-"*150)
"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
G = 6.674 * (10**-11)
def cgravitacion(m1):
    def inferior1(m2):
        m1m2 = m1 * m2
        def inferior2(d):
            d_2 = d**2
            return (G * m1m2) / d_2
        return inferior2
    return inferior1
m1 = 100
m2 = 130
d = 2
F = cgravitacion(m1)(m2)
print(F(2))
##R009##
##40##
"""
Recuerda que todos los ejercicios son opcionales ustedes elegen que 
resolver

Para este ejercicio debes ver primero estos videos

https://www.youtube.com/watch?v=Ku0DRyRjfkk
https://youtu.be/Ku0DRyRjfkk

Lo que ven es un ejemplo de malware muy basico en python,
No quiero que repliquen lo que sucede en el video, pero si notan es 
posible bajar bibliotecas desde pip y pegarlas en una carpeta.

Luego se pueden alterar dichas bibliotecas maliciosamente.
adjunto a este examen hay un par de archivos
XLibrary.py y main.py los cuales funcionan correctamente.

altere el archivo XLibrary.py con un decorador
que de manera aleatoria altere el resultado de <collatz>
agregando el valor -1.5 al final de la lista.
Por lo que el 50% de las veces se modifique la lista y 50% no lo haga.

Espero este codigo les sirva

import random
Moneda = [True,False]
R = random.choice(Moneda)
print(R)
# True
R = random.choice(Moneda)
print(R)
# True
R = random.choice(Moneda)
print(R)
# False
"""
##R010##
##40##
print("-"*150)
print("Pregunta 010")
print("#40#")
print("Respuesta:")
print("-"*150)
"""
Procesar data

Utilizando el patron de diseño composicion por funciones de orden
superior obten la salida correspondiente:

R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = composicion_HOF(R)
T = T(fun0)
T = T(fun1)
T = T(fun2)
T = T(fun3) #...
R = T(lambda e: None)
print(R)
# [3041,30,1000000,"28 de Julio"]

"""

def composicion_HOF(valor):
    print(valor)
    def cadena(fun):
        if not fun:
            return valor
        return composicion_HOF(
            fun(valor)
            )
    return cadena

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

fun0 = lambda cadena: cadena.split(',')

fun1 = lambda lista: [lista[1], lista[2:10], lista[10], lista[11]]

fun2 = lambda lista: [int(lista[0]), list(map(int, lista[1])), int(lista[2]), lista[3]]

fun3 = lambda lista: [lista[0], sum(lista[1]), lista[2], lista[3]]

fun4 = lambda lista: [lista[0], lista[1], lista[2], lista[3].split('/')]

fun5 = lambda lista: [lista[0], lista[1], lista[2], lista[3][0] + " de " + meses[int(lista[3][1]) - 1]]

#------------------------------------------------------------------------------------------------
R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = composicion_HOF(R)
T = T(fun0)
T = T(fun1)
T = T(fun2)
T = T(fun3)
T = T(fun4)
T = T(fun5)
R = T(None)
print(R)
##R011##
##10##
print("-"*150)
print("Pregunta 011")
print("#10#")
print("Respuesta:")
print("-"*150)
import random
def generaLista(N):
    if N == 0:
        return []
    return [random.randint(1, 100)] + generaLista(N - 1)

L = generaLista(100)
print("Lista de 100 numeros aleatorios")
print(L)

def sumaLista(L):
    if not L:
        return None
    match L:
        case [P]:
            return P
        case [P, *F]:
            return P + sumaLista(F)

S = sumaLista(L)
print("Resultado sumatoria: ")
print(S)    
"""
Genera un lista de 100 números aleatorios  
y calcula su suma
"""
##R012##
##10##
print("-"*150)
print("Pregunta 012")
print("#10#")
print("Respuesta:")
print("-"*150)
"""
De la lista anterior genera dos listas una con los numeros pares
y otra con lo numero impares
"""

def filtrarPares(L):
    if not L:
        return L
    match L:
        case [P]:
            if P % 2 == 0:
                return [P]
            else:
                return []
        case [P, *F]:
            if P % 2 == 0:
                return [P] + filtrarPares(F)
            else:
                return filtrarPares(F)

def filtrarImpares(L):
    if not L:
        return L
    match L:
        case [P]:
            if P % 2 != 0:
                return [P]
            else:
                return []
        case [P, *F]:
            if P % 2 != 0:
                return [P] + filtrarImpares(F)
            else:
                return filtrarImpares(F)
Pares = filtrarPares(L)
Impares = filtrarImpares(L)
print("Pares")
print(Pares)
print("-"*150)
print("Impares")
print(Impares)
print("-"*150)