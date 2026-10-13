##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print()
"""


def funcionSuperior(texto):
    def funcionInferior():
        return texto

    return funcionInferior


F = funcionSuperior("Un closure es una función que recuerda las variables de la función externa donde fue creada, "
                    "incluso después de que la función externa haya terminado.")
print(F())

##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""


def definicion():
    return ("Un wrapper es una funcion que envuelve a otra funcion para "
            "agregarle comportamiento extra, antes o despues de ejecutarla, "
            "sin modificar el codigo original de la funcion envuelta.")


def mi_wrapper(funcion):
    def envoltorio():
        texto = funcion()
        print(texto)
        return texto

    return envoltorio


definicion_envuelta = mi_wrapper(definicion)
definicion_envuelta()

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

k = 9 * (10 ** 9)


def coulomb(K, q1, q2, r):
    return (K * q1 * q2) / (r ** 2)


# Wrappers para cada medio
def coulombVacio(q1, q2, r):
    return coulomb(k, q1, q2, r)


def coulombAire(q1, q2, r):
    return coulomb(k / 1.00051, q1, q2, r)


def coulombAlumina(q1, q2, r):
    return coulomb(k / 5.9, q1, q2, r)


def coulombPVC(q1, q2, r):
    return coulomb(k / 3.4, q1, q2, r)


def coulombAgua(q1, q2, r):
    return coulomb(k / 81, q1, q2, r)


def coulombGlicerina(q1, q2, r):
    return coulomb(k / 43, q1, q2, r)


# Valores del ejercicio
q1 = 3 * (10 ** -6)
q2 = -8 * (10 ** -6)
r = 2

print("Vacio:", coulombVacio(q1, q2, r), "N")
print("Aire:", coulombAire(q1, q2, r), "N")
print("Alumina:", coulombAlumina(q1, q2, r), "N")
print("PVC:", coulombPVC(q1, q2, r), "N")
print("Agua:", coulombAgua(q1, q2, r), "N")
print("Glicerina:", coulombGlicerina(q1, q2, r), "N"

##R004##
##20##
# 
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C"""


def ccoulomb(K):
    def inferior1(q1):
        def inferior2(q2):
            def inferior3(r):
                return (K * q1 * q2) / (r ** 2)

            return inferior3

        return inferior2

    return inferior1


k = 9 * (10 ** 9)
q1 = 3 * (10 ** -6)
q2 = -8 * (10 ** -6)
r = 2

F0 = ccoulomb(k)
F1 = F0(q1)
F2 = F1(q2)
F3 = F2(r)

print(F3, "N")

# También se puede evaluar directamente
print(ccoulomb(k)(q1)(q2)(r), "N")

##R005##
##20##
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""


def ccoulomb(K):
    def inferior1(q1):
        def inferior2(q2):
            def inferior3(r):
                return (K * q1 * q2) / (r ** 2)

            return inferior3

        return inferior2

    return inferior1


k = 9 * (10 ** 9)
q1 = 3 * (10 ** -6)
q2 = -8 * (10 ** -6)
r = 2

F0 = ccoulomb(k)
F1 = F0(q1)
F2 = F1(q2)
F3 = F2(r)

print(F3, "N")

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

def gravedadAstro(Tipo):
    def Luna(Monto):
        return lambda m1, m2, d: 1.62 * m1 * m2 / d**2

    def Marte(Monto):
        return lambda m1, m2, d: 3.71 * m1 * m2 / d**2

    def Ganimedes(Monto):
        return lambda m1, m2, d: 1.43 * m1 * m2 / d**2

    def Encelado(Monto):
        return lambda m1, m2, d: 0.113 * m1 * m2 / d**2

    def Titan(Monto):
        return lambda m1, m2, d: 1.352 * m1 * m2 / d**2

    def Venus(Monto):
        return lambda m1, m2, d: 8.87 * m1 * m2 / d**2

    match Tipo:
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


m1 = 100
m2 = 130
d = 2

F = gravedadAstro("Luna")(0)
print("Luna:", F(m1, m2, d), "N")

F = gravedadAstro("Marte")(0)
print("Marte:", F(m1, m2, d), "N")

F = gravedadAstro("Ganímedes")(0)
print("Ganímedes:", F(m1, m2, d), "N")

F = gravedadAstro("Encélado")(0)
print("Encélado:", F(m1, m2, d), "N")

F = gravedadAstro("Titan")(0)
print("Titan:", F(m1, m2, d), "N")

F = gravedadAstro("Venus")(0)
print("Venus:", F(m1, m2, d), "N")

##R007##
##20##
"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
def gravitacion(G, m1, m2, d):
    return (G * m1 * m2) / d**2

def pgravitacion(G):
    def inferior1(m1):
        def inferior2(m2):
            def inferior3(d):
                return gravitacion(G, m1, m2, d)
            return inferior3
        return inferior2
    return inferior1

G = 6.674 * 10**-11
m1 = 100
m2 = 130
d = 2

F = pgravitacion(G)(m1)(m2)(d)

print("Fuerza gravitacional:", F, "N")

##R008##
##20##
"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""

def cgravitacion(G):
    def inferior1(m1):
        def inferior2(m2):
            def inferior3(d):
                return (G * m1 * m2) / d**2
            return inferior3
        return inferior2
    return inferior1

G = 6.674 * 10**-11
m1 = 100
m2 = 130
d = 2

F0 = cgravitacion(G)
F1 = F0(m1)
F2 = F1(m2)
F3 = F2(d)

print("Fuerza gravitacional:", F3, "N")
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
##R011##
##10##
"""
Genera un lista de 100 números aleatorios  
y calcula su suma
"""


def prandint(a):
    import random
    def inferior(b):
        return random.randint(a, b)

    return inferior


T = prandint(1)


def generar(N):
    if N == 0:
        return []
    return generar(N - 1) + [T(100)]


L = generar(100)

print("Lista de numeros aleatorios:")
print(L)

print("Suma de los numeros:")
print(sum(L))

##R012##
##10##
"""
De la lista anterior genera dos listas una con los numeros pares
y otra con lo numero impares
"""


def filtrarPares(Lista):
    if not Lista:
        return []
    match Lista:
        case [P, *F]:
            if P % 2 == 0:
                return [P] + filtrarPares(F)
            else:
                return filtrarPares(F)


def filtrarImpares(Lista):
    if not Lista:
        return []
    match Lista:
        case [P, *F]:
            if P % 2 == 0:
                return filtrarImpares(F)
            else:
                return [P] + filtrarImpares(F)


Pares = filtrarPares(L)
Impares = filtrarImpares(L)

print("Numeros pares:", Pares)
print("Numeros impares:", Impares)
