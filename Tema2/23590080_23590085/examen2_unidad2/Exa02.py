print("Guillermo Daniel Lopez Garcia")
print("Leonardo Emmanuel Buendia Ramos")


print("--------------------R001--------------------")
print("--------------------15--------------------")
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print() 
"""
print("Concepto de una closure: Es una funcion que recibe parametros y retorna una funcion\n")

print("--------------------R002--------------------")
print("--------------------15--------------------")
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""
print("Concepto de un wrapper: Es una funcion especialista que encapsula una funcion dentro de otra para no modificar su funcionalida\n")


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

def leyCoulomb(q1, q2, r, Medio):
    K = Medio(k)
    return (K * (q1 * q2)) / r**2


# WRAPPERS 

def coulombVacio(q1, q2, r):
    return leyCoulomb(q1, q2, r, lambda k: k)

def coulombAire(q1, q2, r):
    return leyCoulomb(q1, q2, r, lambda k: k / 1.00051)

def coulombAlumina(q1, q2, r):
    return leyCoulomb(q1, q2, r, lambda k: k / 5.9)

def coulombPVC(q1, q2, r):
    return leyCoulomb(q1, q2, r, lambda k: k / 3.4)

def coulombAgua(q1, q2, r):
    return leyCoulomb(q1, q2, r, lambda k: k / 81)

def coulombGlicerina(q1, q2, r):
    return leyCoulomb(q1, q2, r, lambda k: k / 43)


# Comprobación: q1 = 3×10^-6 C, q2 = -8×10^-6 C, r = 2 m
q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

print("--------------------R003--------------------")
print("--------------------30--------------------")
print("")
print("Vacio:     ", coulombVacio(q1, q2, r), "N")
print("Aire:      ", coulombAire(q1, q2, r), "N")
print("Alumina:   ", coulombAlumina(q1, q2, r), "N")
print("PVC:       ", coulombPVC(q1, q2, r), "N")
print("Agua:      ", coulombAgua(q1, q2, r), "N")
print("Glicerina: ", coulombGlicerina(q1, q2, r), "N")
print("")
print("")

#guarda, especificacion extra sobre un caso
##R004##
##20##
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
k = 9 * (10**9)

def leyCoulomb(K, q1, q2, r):
    return (K * (q1 * q2)) / r**2

def pleyCoulomb(K):
    def inferior1(q1):
        def inferior2(q2):
            def inferior3(r):
                return leyCoulomb(K, q1, q2, r)
            return inferior3
        return inferior2
    return inferior1

q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

print("--------------------R004--------------------")
print("--------------------20--------------------")
print("")
print(pleyCoulomb(k)(q1)(q2)(r))
print("")
print("")

##R005##
##20##
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""

def cleyCoulomb(q1):
    def inferior1(q2):
        qm = (q1 * q2)
        def inferior2(K):
            qk = K * qm
            def inferior3(r):
                rm = r**2
                col = (qk / rm)
                return col
            return inferior3
        return inferior2
    return inferior1

k = 9 * (10**9)
q1 = 3 * (10**-6)
q2 = -8 * (10**-6)
r = 2

print("--------------------R005--------------------")
print("--------------------20--------------------")
print(cleyCoulomb(q1)(q2)(k)(r))
print("")
print("")
    
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

G = (6.67)*10**(-11)
m1 = 100
m2 = 130
d = 2


def calcularGravedad(Astro):
    def Luna(g):
        return (g *(m1*m2)) / d**2
    def Marte(g):
        return (g *(m1*m2)) / d**2
    def Ganímedes(g):
        return (g *(m1*m2)) / d**2
    def Encélado(g):
        return (g *(m1*m2)) / d**2
    def Titan(g):
        return (g *(m1*m2)) / d**2
    def Venus(g):
        return (g *(m1*m2)) / d**2

    match Astro:
        case "Luna":
            return Luna
        case "Marte":
            return Marte
        case "Ganímedes":
            return Ganímedes
        case "Encélado":
            return Encélado
        case "Titan":
            return Titan
        case "Venus":
            return Venus
        case _:
            return lambda g:g # Funcion identidad


print("--------------------R006--------------------")
print("--------------------30--------------------")
print("")
gAstro = calcularGravedad("Luna")
print(gAstro(1.62))
gAstro = calcularGravedad("Marte")
print(gAstro(3.711))
gAstro = calcularGravedad("Ganímedes")
print(gAstro(1.42))
gAstro = calcularGravedad("Encélado")
print(gAstro(0.113))
gAstro = calcularGravedad("Titan")
print(gAstro(1.352))
gAstro = calcularGravedad("Venus")
print(gAstro(8.87))
print("")
print("")


"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia
"""

print("--------------------R007--------------------")
print("--------------------20--------------------")

def calcula_ley(m1,m2,r):
	return(G * (m1 * m2) / (r ** 2))

def pcalcula_ley(m1):
	def inferior1(m2):
		def inferior2(r):
			return calcula_ley(m1,m2,r)
		return inferior2
	return inferior1

G = (6.67)*10**(-11)
m1 = 100
m2 = 130
r = 2
print("Funcion parcializada")
print(pcalcula_ley(m1)(m2)(r))
print("")


"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia
"""

print("--------------------R008--------------------")
print("--------------------20--------------------")

def ccalcula_ley(m1):
	def inferior_curr1(m2):
		m = m1 * m2
		def inferior_curr2(r):
			d = r**2
			return(G * m / d)
		return inferior_curr2
	return inferior_curr1
print("Funcion currificada")
R0 = ccalcula_ley(100)(130)(2)
print(R0)
print("")


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

print("--------------------R009--------------------")
print("--------------------40--------------------")
print("Revisar el archivo main.py para el reactivo de este ejercicio")

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
def composicion(valor):
    def cadena(fun):
        if fun is None:
            return valor
        return composicion(fun(valor))
    return cadena

R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

meses = {
    "01": "Enero",   "02": "Febrero", "03": "Marzo",
    "04": "Abril",   "05": "Mayo",    "06": "Junio",
    "07": "Julio",   "08": "Agosto",  "09": "Septiembre",
    "10": "Octubre", "11": "Noviembre","12": "Diciembre"
}

def fun0(st):
    return st.split(',')

def fun1(lista):
    return [
        int(elemento) if '/' not in elemento else elemento
        for elemento in lista
    ]

def fun2(lista):
    Q1, Q2, *Z, MON, FECH = lista
    return [Q2, sum(Z), MON, FECH]

def fun3(lista):
    Q2, suma, MON, FECH = lista
    dia, mes, anio = FECH.split('/')
    return [Q2, suma, MON, dia + " de " + meses[mes]]


print("--------------------R010--------------------")
print("--------------------40--------------------")

T = composicion(R)
T = T(fun0)
T = T(fun1)
T = T(fun2)
T = T(fun3)
R = T(None)
print(R)
# [3041, 30, 1000000, "28 de Julio"]
print("")
print("")



print("--------------------R011--------------------")
print("--------------------10--------------------")
"""
Genera un lista de 100 números aleatorios  
y calcula su suma

L = [<valor> for <v_iter> in <iterable>] # Mapear info
"""
import random
numeros = [random.randint(1, 100) for i in range(100)]
suma = sum(numeros)
print(numeros)
print("")
print(suma)
L = numeros
print("")


print("--------------------R012--------------------")
print("--------------------10--------------------")
"""
De la lista anterior genera dos listas una con los numeros pares
y otra con lo numero impares
"""
print("Numeros par")
numeros_par = [str(numeros) for numeros in L if numeros % 2 == 0]
print(numeros_par)
print("\nNumeros impar")
numeros_imp = [str(numeros) for numeros in L if numeros % 2 != 0]
print(numeros_imp)

