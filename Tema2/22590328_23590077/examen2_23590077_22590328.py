print('\n######################-EJERCICIO 1-#######################################\n')
##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print()
"""


Rclosure = '''El closure es una función que retorna a una función inferior que se encuentra
anidada dentro de si mismo, tiene la caracteristica de poder memorizar la información de
variables de la función superior aun cuando esta funcion padre ya haya finalizado

Para poder ser considerada un closure debe cumplir con las siguientes condiciones:
    1. Existe una función inferior anidada dentro de una función superior
    2. Existe una referencia de la función inferior a una o más variables declaradas dentro
    de la función superior
    3. La función superior retorna a una función inferior'''
print(Rclosure)


print('\n######################-EJERCICIO 2-#######################################\n')
##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print()
"""


Rwrapper = '''El wrapper o función especializada es una función que trabaja
tomando una función general externa al wrapper y añade lo necesario para
funcionar en un caso especifico, es utilizada cuando se necesita ejecutar
codigo que tiene una base repetitiva con ciertas distinciones segun el caso
esto ayuda a no tener que escribir lo mismo para cada una de los caminos

Para poder ser considerada un wrapper debe cumplir con los siguientes:
    1. Convertir una tarea genérica en una tarea especializada
    2. El trabajo es realizado por la función general mientras que la especializada
    generalmente solo define variables y coloca condiciones (suele ser mucho mas corta)
'''
print(Rwrapper)


print('\n######################-EJERCICIO 3-#######################################\n')
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

def coulomb(K, q1, q2, r):
    return (K * q1 * q2) / r**2


def coulomb_vacio(q1, q2, r):
    return coulomb(k, q1, q2, r)


def coulomb_aire(q1, q2, r):
    return coulomb(k / 1.00051, q1, q2, r)


def coulomb_alumina(q1, q2, r):
    return coulomb(k / 5.9, q1, q2, r)


def coulomb_pvc(q1, q2, r):
    return coulomb(k / 3.4, q1, q2, r)


def coulomb_agua(q1, q2, r):
    return coulomb(k / 81, q1, q2, r)


def coulomb_glicerina(q1, q2, r):
    return coulomb(k / 43, q1, q2, r)


q1, q2, r = 3e-6, -8e-6, 2

print("Vacío:     ", coulomb_vacio(q1, q2, r))
print("Aire:      ", coulomb_aire(q1, q2, r))
print("Alúmina:   ", coulomb_alumina(q1, q2, r))
print("PVC:       ", coulomb_pvc(q1, q2, r))
print("Agua:      ", coulomb_agua(q1, q2, r))
print("Glicerina: ", coulomb_glicerina(q1, q2, r))



print('\n######################-EJERCICIO 4-#######################################\n')
##R004##
##20##
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
# Función general: Ley de Coulomb  F = K * (q1 * q2) / r**2
def coulomb(Q1, Q2, R):
    K = 9e9  # constante de Coulomb en N·m²/C²
    return K * (Q1 * Q2) / R**2


def pcoulomb(Q1):
    def inferior1(Q2):
        def inferior2(R):
            return coulomb(Q1, Q2, R)
        return inferior2
    return inferior1
# Comprobación: q1 = 3×10^-6 C, q2 = -8×10^-6 C, r = 2 m
F0 = pcoulomb(3e-6)
F1 = F0(-8e-6)
F = F1(2)
print(F)
# -0.054

R0 = pcoulomb(3e-6)(-8e-6)(2)
print(R0)
# -0.054



print('\n######################-EJERCICIO 5-#######################################\n')
##R005##
##20##
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""

def ccoulomb(Q1):
    K = 9e9
    KQ1 = K * Q1
    def inferior1(Q2):
        KQ1Q2 = KQ1 * Q2
        def inferior2(R):
            R_2 = R ** 2
            return KQ1Q2 / R_2
        return inferior2
    return inferior1


F = ccoulomb(3e-6)(-8e-6)(2)
print(F)
# -0.054





print('\n######################-EJERCICIO 6-#######################################\n')
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

GRAVEDADES = {
    "Luna": 1.62,
    "Marte": 3.711,
    "Ganimedes": 1.42,
    "Encelado": 0.113,
    "Titan": 1.352,
    "Venus": 8.87,
}


def gravitacion(astro):
    G = GRAVEDADES[astro]  # variable capturada por el closure

    def calcula(m1, m2, d):
        return (G * m1 * m2) / d**2

    return calcula


m1, m2, d = 100, 130, 2
for astro in GRAVEDADES:
    F = gravitacion(astro)  # closure: recuerda G aunque gravitacion() ya terminó
    print(astro, F(m1, m2, d))


print('\n######################-EJERCICIO 7-#######################################\n')
##R007##
##20##
"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
# Función general: F = (G*(m1*m2)) / d**2
def gravitacion(M1, M2, D):
    G = 6.674e-11  # constante de gravitación universal en N·m²/kg²
    return (G * (M1 * M2)) / D**2


# Función parcializada: un nivel por parámetro,
# el último nivel llama a la función general
def pgravitacion(M1):
    def inferior1(M2):
        def inferior2(D):
            return gravitacion(M1, M2, D)
        return inferior2
    return inferior1


# Comprobación: m1 = 100 kg, m2 = 130 kg, d = 2 m
F0 = pgravitacion(100)
F1 = F0(130)
F = F1(2)
print(F)
# 2.16905e-07

R0 = pgravitacion(100)(130)(2)
print(R0)
# 2.16905e-07

print('\n######################-EJERCICIO 8-#######################################\n')
##R008##
##20##
"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""

def cgravitacion(M1):
    G = 6.674e-11
    GM1 = G * M1              
    def inferior1(M2):
        GM1M2 = GM1 * M2        
        def inferior2(D):
            D_2 = D ** 2        
            return GM1M2 / D_2
        return inferior2
    return inferior1


# Comprobación: m1 = 100 kg, m2 = 130 kg, d = 2 m
F0 = cgravitacion(100)
F1 = F0(130)
F = F1(2)
print(F)
# 2.16905e-07

R0 = cgravitacion(100)(130)(2)
print(R0)
# 2.16905e-07



print('\n######################-EJERCICIO 9-#######################################\n')
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


print('\n######################-EJERCICIO 10-#######################################\n')
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
R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def composicion_HOF(valor):
    def aplicar(f):
        resultado = f(valor)
        if resultado is None:        
            return valor
        return composicion_HOF(resultado) 
    return aplicar


# Cada paso es una función pequeña y reutilizable
def fun0(s):
    # "20,3041,...,28/07/2026" -> ["20", "3041", ..., "28/07/2026"]
    return s.split(",")


def fun1(L):
    # convierte a int todo menos la fecha (último elemento)
    return [int(x) for x in L[:-1]] + [L[-1]]


def fun2(L):
    # se queda con: 3041, suma de los 8 números centrales, 1000000 y la fecha
    return [L[1], sum(L[2:10]), L[10], L[11]]


def fun3(L):
    # "28/07/2026" -> "28 de Julio"
    dia, mes, _ = L[3].split("/")
    return L[:3] + [f"{int(dia)} de {MESES[int(mes) - 1]}"]


T = composicion_HOF(R)
T = T(fun0)
T = T(fun1)
T = T(fun2)
T = T(fun3)
R = T(lambda e: None)
print(R)
# [3041, 30, 1000000, '28 de Julio']




print('######################-EJERCICIO 11-#######################################\n')
##R011##
##10##
"""
Genera un lista de 100 números aleatorios  
y calcula su suma
"""
def a100random(a):
    def random100(b):
        import random
        return [random.randint(a, b) for numero in range(100)]
    return random100

#Generar la lista con 100 numeros aleatorios
print('lista de 100 numeros aleatorios entre 1 y 10')
T = a100random(1)
R = T(10)
print(R)
#Calcula la suma de los 100 numeros aleatorios
print('La suma de los 100 numeros aleatorios')
print(sum(R))

print('\n######################-EJERCICIO 12-#######################################\n')
##R012##
##10##
"""
De la lista anterior genera dos listas una con los numeros pares
y otra con lo numero impares
"""


##############################################
# Función general => Función de caso general #
##############################################
def filtrar(Lista, Funcion):  
    if not Lista:
        return []
    match Lista:
        case [P]:
            if Funcion(P): 
                return [P]
            return []
        case [P,*F]:
              if Funcion(P):
                return [P] + filtrar(F,Funcion)
              return filtrar(F,Funcion)
        case _:
            return []

####################################################
# Wrapper ==> Funcion especialista o especializada #
####################################################
def filtraPorPares(Lista):
    return filtrar(Lista,lambda P : P % 2 == 0)

def filtraPorImpar(Lista):
    return filtrar(Lista,lambda P : P % 2 != 0)

print('Lista numeros pares')
print(filtraPorPares(R))
print('Lista numeros impares')
print(filtraPorImpar(R))
        
print('\n######################- FIN -#######################################\n')