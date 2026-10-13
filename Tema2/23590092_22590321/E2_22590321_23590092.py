##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print() 
"""
cadena_1 = '''Un closure es una funcion, la cual conserva el acceso a las variables del entorno en 
el que fue creada, incluso cuando la funcion externa ya termino de ejecutarse en otras palabras, 
permite que una funcion interna utiilice variables de una funcion externa sin necesidad de recibirlas nuevamente.'''

print(cadena_1)

##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""
cadena_2 = '''
Un wrapper es una funcion que envuelve a otra para facilitar su uso o agregarle funcionalidades
adicionales sin modificar directamente su codigo original
'''

print(cadena_2)

##R003##
##30##
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

# Funcion principal
def coulomb(q1, q2, r, K):
    return (K * (q1 * q2)) / (r**2)

# Wrapper 1: Vacio
def vacio(q1, q2, r):
    return coulomb(q1, q2, r, k)

# Wrapper 2: Aire
def aire(q1, q2, r):
    return coulomb(q1, q2, r, k / 1.00051)

# Wrapper 3: Alúmina
def alumina(q1, q2, r):
    return coulomb(q1, q2, r, k / 5.9)

# Wrapper 4: PVC
def pvc(q1, q2, r):
    return coulomb(q1, q2, r, k / 3.4)

# Wrapper 5: Agua
def agua(q1, q2, r):
    return coulomb(q1, q2, r, k / 81)

# Wrapper 6: Glicerina
def glicerina(q1, q2, r):
    return coulomb(q1, q2, r, k / 43)

# Valores del ejercicio
q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

# Resultados
print("Vacio:", vacio(q1, q2, r))
print("Aire:", aire(q1, q2, r))
print("Alumina:", alumina(q1, q2, r))
print("PVC:", pvc(q1, q2, r))
print("Agua:", agua(q1, q2, r))
print("Glicerina:", glicerina(q1, q2, r))

##R004##
##20##
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
k = 9 * (10**9)

# Funcion de la Ley de Coulomb
def coulomb(q1, q2, r, K):
    return (K * (q1 * q2)) / (r**2)

def coulomb_vacio(q1, q2, r):
    return coulomb(q1, q2, r, k)

q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

# Comprobacion
print(coulomb_vacio(q1, q2, r))

##R005##
##20##
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
k = 9 * (10**9)
def coulomb(q1):
    def carga2(q2):
        def distancia(r):
            def constante(K):
                return (K * (q1 * q2)) / (r**2)
            return constante
        return distancia
    return carga2

q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

# Comprobacion de la currificacion
resultado = coulomb(q1)(q2)(r)(k)

print(resultado)

##R006##
##30##
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

def calcularGravedad(Astro):
    def Luna(m1, m2, d):
        return (1.62 * (m1 * m2)) / d**2
    def Marte(m1, m2, d):
        return (3.711 * (m1 * m2)) / d**2
    def Ganimedes(m1, m2, d):
        return (1.42 * (m1 * m2)) / d**2
    def Encelado(m1, m2, d):
        return (0.113 * (m1 * m2)) / d**2
    def Titan(m1, m2, d):
        return (1.352 * (m1 * m2)) / d**2
    def Venus(m1, m2, d):
        return (8.87 * (m1 * m2)) / d**2

    match Astro:
        case "Luna":
            return Luna
        case "Marte":
            return Marte
        case "Ganimedes":
            return Ganimedes
        case "Encelado":
            return Encelado
        case "Titan":
            return Titan
        case "Venus":
            return Venus
        case _:
            return lambda m1, m2, d: 0
        
R = calcularGravedad("Luna")(100, 130, 2)
print("Luna:", R)
R = calcularGravedad("Marte")(100, 130, 2)
print("Marte:", R)
R = calcularGravedad("Ganimedes")(100, 130, 2)
print("Ganimedes:", R)
R = calcularGravedad("Encelado")(100, 130, 2)
print("Encelado:", R)
R = calcularGravedad("Titan")(100, 130, 2)
print("Titan:", R)
R = calcularGravedad("Venus")(100, 130, 2)
print("Venus:", R)

##R007##
##20##
"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
def gravitacion(m1, m2, d):
    G = 6.674 * (10**-11)
    return (G * (m1 * m2)) / d**2

def pgravitacion(m1):
    def inferior1(m2):
        def inferior2(d):
            return gravitacion(m1, m2, d)
        return inferior2
    return inferior1

R = pgravitacion(100)(130)(2)
print(R)

##R008##
##20##
"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
def Cgravitacion(m1):
    G = 6.674 * (10**-11)
    def inferior1(m2):
        M = m1 * m2
        def inferior2(d):
            return (G * M) / d**2
        return inferior2
    return inferior1

R = Cgravitacion(100)(130)(2)
print(R)

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
    def cadena(fun):
        if not fun:
            return valor
        R = fun(valor)
        if R is None:
            return valor
        return composicion_HOF(R)
    return cadena


def fun0(st):
    return st.strip()

def fun1(st):
    return st.split(',')

def fun2(iterable):
    return [
        int(elemento) if not '/' in elemento else elemento
        for elemento in iterable
    ]

def fun3(lista):
    Q1, Q2, *Z, MON, FECH = lista
    DIA, MES, ANIO = FECH.split('/')
    match MES:
        case "01":
            MES = "Enero"
        case "02":
            MES = "Febrero"
        case "03":
            MES = "Marzo"
        case "04":
            MES = "Abril"
        case "05":
            MES = "Mayo"
        case "06":
            MES = "Junio"
        case "07":
            MES = "Julio"
        case "08":
            MES = "Agosto"
        case "09":
            MES = "Septiembre"
        case "10":
            MES = "Octubre"
        case "11":
            MES = "Noviembre"
        case "12":
            MES = "Diciembre"
    return [Q2] + [sum(Z)] + [MON, DIA + " de " + MES]

R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = composicion_HOF(R)
T = T(fun0)
T = T(fun1)
T = T(fun2)
T = T(fun3)

R = T(lambda e: None)
print(R)

##R011##
##10##
"""
Genera un lista de 100 números aleatorios  
y calcula su suma
"""
import random

Lista = [random.randint(1, 100) for N in range(100)]

print(Lista)
print(sum(Lista))

##R012##
##10##
"""
De la lista anterior genera dos listas una con los numeros pares
y otra con lo numero impares
"""

def filtrar(Lista, Funcion):
    if not Lista:
        return []
    match Lista:
        case [P]:
            if Funcion(P):
                return [P]
            return []
        case [P, *F]:
            if Funcion(P):
                return [P] + filtrar(F, Funcion)
            return filtrar(F, Funcion)
        case _:
            return []

Pares = filtrar(Lista, lambda P: P % 2 == 0)
Impares = filtrar(Lista, lambda P: P % 2 != 0)

print("Lista original:")
print(Lista)
print("Numeros pares:")
print(Pares)
print("Numeros impares:")
print(Impares)
