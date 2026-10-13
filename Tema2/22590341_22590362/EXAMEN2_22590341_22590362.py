##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print() 
"""
print("Reactivo 001\n Un closure es una funcion que regresa a otra funcion ")

##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print() 
"""
print("Reactivo 002\n Un wrapper es una funcion que se desprende de una funcion de \n caso general y es una funcion especailizada o pensada para un caso en particular")

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

#Funcion general => Funcion de caso general
def Coulomb(K, q1, q2, r):
    return ((K*(q1 * q2))/r**2)  

#Wrapper => Funcion especialista o especializada
def Vacio(q1, q2, r):
    return Coulomb(.009, q1, q2, r)
def Aire(q1, q2, r):
    return Coulomb(.009/1.00051, q1, q2, r)
def Aluminia(q1, q2, r):
    return Coulomb(.009/5.9, q1, q2, r)
def PVC(q1, q2, r):
    return Coulomb(.009/3.4, q1, q2, r)
def Agua(q1, q2, r):
    return Coulomb(.009/81, q1, q2, r)
def Glicerina(q1, q2, r):
    return Coulomb(.009/43, q1, q2, r)

print ("Reactivo 003")
print(Vacio(3,-8,2))



##R004##
##20##
"""
Elabora una parcialización de la función que resuelva la Ley de Coulomb.
Compruebe la parcializacion considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""

#Funcion general
def calculaC(Tipo,q1,q2,r):
    match Tipo:
        case "Vacio":
            K = 0.009
            return ((K*(q1 * q2))/r**2)
        case "Aire":
            K = 0.009/1.00051
            return ((K*(q1 * q2))/r**2)
        case "Aluminia":
            K = 0.009/5.9
            return ((K*(q1 * q2))/r**2)
        case "PVC":
            K = 0.009/3.4
            return ((K*(q1 * q2))/r**2)
        case "Agua":
            K = 0.009/81
            return ((K*(q1 * q2))/r**2)
        case "Glicerina":
            K = 0.009/43
            return ((K*(q1 * q2))/r**2)


#Funcion parcializada
def pcalculaC(tipo):
    def step1(q1):
        def step2(q2):
            def step3(r):
                return calculaC(tipo,q1,q2,r)
            return step3
        return step2
    return step1
print ("Reactivo 004")
print("--- PARCIALIZADA ---")
R4 = pcalculaC("Vacio")(3)(-8)(2)
print(R4)



##R005##
##20##
"""
Elabora una currificación de la función que resuelva la Ley de Coulomb.
Compruebe la currificación considerando que una carga de 3×10^-6 C 
se encuentra 2 m de una carga de -8×10^-6 C
"""

def  pdistancia3D(Tipo):
    if Tipo == "Vacio":
        K = 0.009
    if Tipo == "Aire":
        K = 0.009/1.00051
    if Tipo == "Aluminia":
        K =  0.009/5.9
    if Tipo == "PVC":
        K = 0.009/3.4
    if Tipo == "Agua":
        K = 0.009/81
    if Tipo == "Glicerina":
        K = 0.009/43
    def step1(q1):
        def step2(q2):
            qx=q1*q2
            def step3(r):
                r_cuad=r**2
                F = (K*qx)/r_cuad
                return F
            return step3
        return step2
    return step1

print ("Reactivo 005")
print("--- CURRIFICADA ---")
R5 = pdistancia3D ("Vacio")(3)(-8)(2)
print(R5)

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


def FuncionLeyG(astro):
	def Luna (m1,m2,d):
		return (1.62 *(m1*m2)) / d**2
	def Marte (m1,m2,d):
		return (3.711*(m1*m2)) / d**2
	def Ganimedes(m1,m2,d):
		return(1.42 *(m1*m2)) / d**2
	def Encelado(m1,m2,d):
		return (0.113 *(m1*m2)) / d**2
	def Titan(m1,m2,d):
		return (1.352 *(m1*m2)) / d**2
	def Venus(m1,m2,d):
		return (8.87 *(m1*m2)) / d**2
		
	match astro:
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
	
m1=100
m2=130
d=2
print ("Reactivo 006")
print("--- CLOSURE ---")
R6=FuncionLeyG("Luna")
print(R6(m1,m2,d))
R6=FuncionLeyG("Marte")
print(R6(m1,m2,d))
R6=FuncionLeyG("Ganimedes")
print(R6(m1,m2,d))
R6=FuncionLeyG("Encelado")
print(R6(m1,m2,d))
R6=FuncionLeyG("Titan")
print(R6(m1,m2,d))
R6=FuncionLeyG("Venus")
print(R6(m1,m2,d))

##R007##
##20##
"""
Elabora una parcialización de una función que resuelva la ley de
la gravitacion universal.
Compruebe la parcializacion considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""
def pFuncionLeyG(g, m1, m2, d):
	return (g * (m1 * m2)) / (d**2)
	
def p_FuncionLeyG(astro):
	if astro == "Luna":
		g = 1.62
	if astro == "Marte": 
		g = 3.711
	if astro == "Ganimedes": 
		g = 1.42
	if astro == "Encelado":
		g = 0.113
	if astro == "Titan":
		g = 1.352
	if astro == "Venus":
		g = 8.87
		 
	def inferior1(m1):
		def inferior2(m2):
			def inferior3(d):
				return pFuncionLeyG(g, m1, m2, d)
			return inferior3
		return inferior2
	return inferior1
m1 = 100
m2 = 130
d = 2
print ("Reactivo 007")
print("--- PARCIALIZADA ---")
R7 = p_FuncionLeyG("Luna")(m1)(m2)(d)
print("Luna:", R7)
R7 = p_FuncionLeyG("Marte")(m1)(m2)(d)
print("Marte:", R7)
R7 = p_FuncionLeyG("Ganimedes")(m1)(m2)(d)
print("Ganimedes:", R7)
R7 = p_FuncionLeyG("Encelado")(m1)(m2)(d)
print("Encelado:", R7)
R7 = p_FuncionLeyG("Titan")(m1)(m2)(d)
print("Titan:", R7)
R7 = p_FuncionLeyG("Venus")(m1)(m2)(d)
print("Venus:", R7)

##R008##
##20##
"""
Elabora una currificación de una función que resuelva la ley de
la gravitacion universal.
Compruebe la currificación considerando dos masas de 100kg y 130kg 
a 2 metros de distancia

"""


def c_FuncionLeyG(astro):
	if astro == "Luna": g = 1.62
	if astro == "Marte": g = 3.711
	if astro == "Ganimedes": g = 1.42
	if astro == "Encelado": g = 0.113
	if astro == "Titan": g = 1.352
	if astro == "Venus": g = 8.87

	def inferior1(m1):
		def inferior2(m2):
			M = m1 * m2
			def inferior3(d):
				D_2 = d**2
				F = (g * M) / D_2
				return F
			return inferior3
		return inferior2
	return inferior1

# --- COMPROBACIÓN ---
m1 = 100
m2 = 130
d = 2
print ("Reactivo 007")
print("--- CURRIFICADA ---")

R8 = c_FuncionLeyG("Luna")(m1)(m2)(d)
print("Luna: ", R8)
R8 = c_FuncionLeyG("Marte")(m1)(m2)(d)
print("Marte:", R8)
R8 = c_FuncionLeyG("Ganimedes")(m1)(m2)(d)
print("Ganimedes:", R8)
R8 = c_FuncionLeyG("Encelado")(m1)(m2)(d)
print("Encelado:", R8)
R8 = c_FuncionLeyG("Titan")(m1)(m2)(d)
print("Titan:", R8)
R8 = c_FuncionLeyG("Venus")(m1)(m2)(d)
print("Venus:", R8)
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
