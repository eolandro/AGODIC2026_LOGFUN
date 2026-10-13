#Oliver Uriel Pagola Perez 23590114
#Javier Yael Enriquez Martinez 22590324

##R001##
##15##
concepto_closure = """Un closure es una funcion de orden superior que retorna 
una funcion interna permitiendo que esta ultima recuerde y acceda a las variables 
de la funcion superior incluso despues de que haya terminado 
su ejecución."""
print(concepto_closure)
#--------------------------------------------------------------
##R002##
##15##
concepto_wrapper = """Un wrapper es una funcion que envuelve 
a una funcion mas general Sirve para fijar ciertos parametros o especializar su 
comportamiento sin tener que reescribir la logica principal, promoviendo la 
reutilizacion del codigo puro."""
print(concepto_wrapper)

#--------------------------------------------------------------
##R004##
##20##
def p_coulomb(K):
    def inferior1(q1):
        def inferior2(q2):
            def inferior3(r):
                return (K * (q1 * q2)) / (r ** 2)
            return inferior3
        return inferior2
    return inferior1

# K = 9e9, q1 = 3e-6, q2 = -8e-6, r = 2
F_parcial = p_coulomb(9e9)(3e-6)(-8e-6)(2)
print(F_parcial)

#--------------------------------------------------------------
##R005##
##20##
def c_coulomb(K):
    def inferior1(q1):
        K_q1 = K * q1
        def inferior2(q2):
            K_q1_q2 = K_q1 * q2
            def inferior3(r):
                r_2 = r ** 2
                return K_q1_q2 / r_2
            return inferior3
        return inferior2
    return inferior1

F_curry = c_coulomb(9e9)(3e-6)(-8e-6)(2)
print(F_curry)
#--------------------------------------------------------------
##R006##
##30##
def fuerzaGravitacional(astro):

    def con_gravedad(g):
        return lambda m1, m2, d: (g * (m1 * m2)) / d ** 2

    match astro:
        case "Luna":
            return con_gravedad(1.62)
        case "Marte":
            return con_gravedad(3.711)
        case "Ganimedes":
            return con_gravedad(1.42)
        case "Encelado":
            return con_gravedad(0.113)
        case "Titan":
            return con_gravedad(1.352)
        case "Venus":
            return con_gravedad(8.87)
        case _:
            return None


M1 = 100
M2 = 130
D = 2


def probar(astros):
    match astros:
        case []:
            return None
        case [astro, *resto]:
            print(astro, fuerzaGravitacional(astro)(M1, M2, D))
            return probar(resto)
        case _:
            return None


probar(["Luna", "Marte", "Ganimedes", "Encelado", "Titan", "Venus"])

# Luna: 5265.0
# Marte: 12060.75
# Ganimedes: 4615.0
# Encelado: 367.25
# Titan: 4394.0
# Venus: 28827.499999999996

#--------------------------------------------------------------
##R007##
##20##
# Parcialización pura para Gravitación
def p_gravitacion(G):
    def inferior1(m1):
        def inferior2(m2):
            def inferior3(d):
                return (G * (m1 * m2)) / (d ** 2)
            return inferior3
        return inferior2
    return inferior1

#mG = 6.674e-11, m1 = 100, m2 = 130, d = 2
F_grav_p = p_gravitacion(6.674e-11)(100)(130)(2)
print(F_grav_p)

#--------------------------------------------------------------
##R008##
##20##
def c_gravitacion(G):
    def inferior1(m1):
        G_m1 = G * m1
        def inferior2(m2):
            G_m1_m2 = G_m1 * m2
            def inferior3(d):
                d_2 = d ** 2
                return G_m1_m2 / d_2
            return inferior3
        return inferior2
    return inferior1
F_grav_c = c_gravitacion(6.674e-11)(100)(130)(2)
print(F_grav_c)

#--------------------------------------------------------------


##R011##
##10##
import random
def generar_aleatorios(limite):
    if limite == 0:
        return []
    return [random.randint(1, 1000)] + generar_aleatorios(limite - 1)

def suma_lista(L):
    match L:
        case []:
            return 0
        case [P, *F]:
            return P + suma_lista(F)
        case _:
            return 0
            
lista_100 = generar_aleatorios(100)
suma_total = suma_lista(lista_100)
print(suma_total)

#--------------------------------------------------------------
##R012##
##10##
# Filtrado por patrón estructural y recursión pura
def filtrar_pares(L):
    match L:
        case []:
            return []
        case [P, *F] if P % 2 == 0:
            return [P] + filtrar_pares(F)
        case [_, *F]:
            return filtrar_pares(F)

def filtrar_impares(L):
    match L:
        case []:
            return []
        case [P, *F] if P % 2 != 0:
            return [P] + filtrar_impares(F)
        case [_, *F]:
            return filtrar_impares(F)

pares = filtrar_pares(lista_100)
impares = filtrar_impares(lista_100)

print(pares)
print(impares)
