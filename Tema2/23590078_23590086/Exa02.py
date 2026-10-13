##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print() 
"""
print("##R001##")
print("closure es una función que me retorna a otra función, generalmente solo tiene 2 niveles")


##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""
print("##R002##")
print("Un wrapper es un caso especifico de una función general que por lo general es mucho mas corta")
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
print(" ")
print("##R003##")

k = 9 * (10 ** 9)

def Ley_Coulomb(q1, q2, r, medio):
	constantes = {
		"vacio": k,
		"aire": k / 1.00051,
		"alumina": k / 5.9,
		"pvc": k / 3.4,
		"agua": k / 81,
		"glicerina": k / 43
	}
	K = constantes[medio]
	F = (K * q1 * q2) / (r ** 2)
	return F

def vacio(q1, q2, r):
	return Ley_Coulomb(q1, q2, r, "vacio")

def aire(q1, q2, r):
	return Ley_Coulomb(q1, q2, r, "aire")

def alumina(q1, q2, r):
	return Ley_Coulomb(q1, q2, r, "alumina")

def pvc(q1, q2, r):
	return Ley_Coulomb(q1, q2, r, "pvc")

def agua(q1, q2, r):
	return Ley_Coulomb(q1, q2, r, "agua")

def glicerina(q1, q2, r):
	return Ley_Coulomb(q1, q2, r, "glicerina")
"""
q1 = 3 * (10 ** -6)
q2 = -8 * (10 ** -6)
r = 2
print("Vacio:", vacio(q1, q2, r))
print("Aire:", aire(q1, q2, r))
print("Alumina:", alumina(q1, q2, r))
print("PVC:", pvc(q1, q2, r))
print("Agua:", agua(q1, q2, r))
print("Glicerina:", glicerina(q1, q2, r))
"""
print(" ")

##R004##
##20##
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
print(" ")
print("##R004##")
def pLey_Coulomb(q1):
	def inferior1(q2):
		def inferior2(r):
			def inferior3(medio):
				return Ley_Coulomb(q1, q2, r, medio)
			return inferior3
		return inferior2
	return inferior1
"""
q1 = 3 * (10 ** -6)
q2 = -8 * (10 ** -6)
r = 2
print("Vacio:", pLey_Coulomb(q1)(q2)(r)("vacio"))
print("Aire:", pLey_Coulomb(q1)(q2)(r)("aire"))
print("Alumina:", pLey_Coulomb(q1)(q2)(r)("alumina"))
print("PVC:", pLey_Coulomb(q1)(q2)(r)("pvc"))
print("Agua:", pLey_Coulomb(q1)(q2)(r)("agua"))
print("Glicerina:", pLey_Coulomb(q1)(q2)(r)("glicerina"))
"""
print(" ")
##R005##
##20##
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""
print(" ")
print("##R005##")

def Ccoulomb(q1):
	constantes = {
		"vacio": k,
		"aire": k / 1.00051,
		"alumina": k / 5.9,
		"pvc": k / 3.4,
		"agua": k / 81,
		"glicerina": k / 43
	}
	def inferior1(q2):
		Q = q1 * q2
		def inferior2(r):
			r_2 = r ** 2
			def inferior3(medio):
				K = constantes[medio]
				return (K * Q) / r_2
			return inferior3
		return inferior2
	return inferior1

q1 = 3 * (10 ** -6)
q2 = -8 * (10 ** -6)
r = 2

print("Vacio:", Ccoulomb(q1)(q2)(r)("vacio"))
print("Aire:", Ccoulomb(q1)(q2)(r)("aire"))
print("Alumina:", Ccoulomb(q1)(q2)(r)("alumina"))
print("PVC:", Ccoulomb(q1)(q2)(r)("pvc"))
print("Agua:", Ccoulomb(q1)(q2)(r)("agua"))
print("Glicerina:", Ccoulomb(q1)(q2)(r)("glicerina"))

print(" ")
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
print(" ")
print("##R006##")
def crear_gravedad(gravedad):
    def fuerza(masa):
        return masa * gravedad
    return fuerza

luna = crear_gravedad(1.62)
marte = crear_gravedad(3.711)
ganimedes = crear_gravedad(1.42)
encelado = crear_gravedad(0.113)
titan = crear_gravedad(1.352)
venus = crear_gravedad(8.87)

print("Luna")
print("Fuerza para 100 kg:", luna(100), "N")
print("Fuerza para 130 kg:", luna(130), "N")

print("\nMarte")
print("Fuerza para 100 kg:", marte(100), "N")
print("Fuerza para 130 kg:", marte(130), "N")

print("\nGanímedes")
print("Fuerza para 100 kg:", ganimedes(100), "N")
print("Fuerza para 130 kg:", ganimedes(130), "N")

print("\nEncélado")
print("Fuerza para 100 kg:", encelado(100), "N")
print("Fuerza para 130 kg:", encelado(130), "N")

print("\nTitán")
print("Fuerza para 100 kg:", titan(100), "N")
print("Fuerza para 130 kg:", titan(130), "N")

print("\nVenus")
print("Fuerza para 100 kg:", venus(100), "N")
print("Fuerza para 130 kg:", venus(130), "N")
print(" ")
##R007##
##20##
"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
print(" ")
print("##R007##")
from functools import partial
G = 6.67430e-11

def gravitacion(m1,m2,d):
	return (G * m1 * m2) / d**2
	
calcular = partial(gravitacion, 100, 130)

resultado = calcular(2)

print("Fuerza gravitacional: ", resultado, "N")
print(" ")
##R008##
##20##
"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
print(" ")
print("##R008##")
def gravitacion(m1):
	def masa2(m2):
		def distancia(d):
			return (G * m1 * m2) / d**2
		return distancia
	return masa2

resultado = gravitacion(100)(130)(2)

print("Fuerza gravitatoria: ", resultado, "N")
print(" ")
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
##R012##
##10##
"""
De la lista anterior genera dos listas una con los numeros pares
y otra con lo numero impares
"""
