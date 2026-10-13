import random

##R001##
##15##
"""
Define con tus palabras el concepto de una closure
colocalo en una cadena y usa print()
"""
closure = (
    "Una closure es una funcion interna que recuerda el entorno (las "
    "variables) de la funcion externa donde fue creada, aunque esa "
    "funcion externa ya haya terminado. Por eso sigue usando esos "
    "valores cada vez que se la llama."
)
print(closure)


##R002##
##15##
"""
Define con tus palabras el concepto de un wrapper
colocalo en una cadena y usa print()
"""
wrapper = (
    "Un wrapper es una funcion especialista que envuelve a una funcion "
    "general y le fija algunos de sus valores, sin modificarla. Sirve "
    "para reutilizar la funcion general en un caso mas especifico."
)
print(wrapper)


##R003##
##30##
"""
Ley de Coulomb
F = (K*(q1 * q2)) / r**2
k = 9 * (10**9)
6 wrappers, uno por cada medio.
Prueba: q1 = 3e-6 C, q2 = -8e-6 C, r = 2 m
"""
k = 9 * (10 ** 9)


def coulomb(q1, q2, r, K):
    return (K * (q1 * q2)) / r ** 2


def coulomb_vacio(q1, q2, r):
    return coulomb(q1, q2, r, k)


def coulomb_aire(q1, q2, r):
    return coulomb(q1, q2, r, k / 1.00051)


def coulomb_alumina(q1, q2, r):
    return coulomb(q1, q2, r, k / 5.9)


def coulomb_pvc(q1, q2, r):
    return coulomb(q1, q2, r, k / 3.4)


def coulomb_agua(q1, q2, r):
    return coulomb(q1, q2, r, k / 81)


def coulomb_glicerina(q1, q2, r):
    return coulomb(q1, q2, r, k / 43)


##R004##
##20##
"""
Parcializacion de la Ley de Coulomb: un argumento por nivel,
el nivel final llama a la funcion general.
"""
def pcoulomb(q1):
    def inferior1(q2):
        def inferior2(r):
            def inferior3(K):
                return coulomb(q1, q2, r, K)
            return inferior3
        return inferior2
    return inferior1


##R005##
##20##
"""
Currificacion de la Ley de Coulomb: un argumento por nivel,
precalculando en cada nivel (no llama a la general).
"""
def ccoulomb(q1):
    def inferior1(q2):
        q1q2 = q1 * q2
        def inferior2(r):
            r2 = r ** 2
            def inferior3(K):
                return (K * q1q2) / r2
            return inferior3
        return inferior2
    return inferior1


##R006##
##30##
"""
Ley de la Gravitacion universal
Closure que, segun el nombre del astro, retorna la funcion con la
gravedad adecuada.
Prueba: m1 = 100 kg, m2 = 130 kg, d = 2 m
"""
def calcular_gravedad(Astro):
    def luna(m1, m2, d):
        return (1.62 * (m1 * m2)) / d ** 2

    def marte(m1, m2, d):
        return (3.711 * (m1 * m2)) / d ** 2

    def ganimedes(m1, m2, d):
        return (1.42 * (m1 * m2)) / d ** 2

    def encelado(m1, m2, d):
        return (0.113 * (m1 * m2)) / d ** 2

    def titan(m1, m2, d):
        return (1.352 * (m1 * m2)) / d ** 2

    def venus(m1, m2, d):
        return (8.87 * (m1 * m2)) / d ** 2

    match Astro:
        case "Luna":
            return luna
        case "Marte":
            return marte
        case "Ganimedes":
            return ganimedes
        case "Encelado":
            return encelado
        case "Titan":
            return titan
        case "Venus":
            return venus
        case _:
            return None


##R007##
##20##
"""
Parcializacion de la ley de la gravitacion universal.
F = (G*(m1*m2)) / d**2
Prueba: m1 = 100 kg, m2 = 130 kg, d = 2 m
"""
G = 6.674 * (10 ** -11)


def gravitacion(m1, m2, d):
    return (G * (m1 * m2)) / d ** 2


def pgravitacion(m1):
    def inferior1(m2):
        def inferior2(d):
            return gravitacion(m1, m2, d)
        return inferior2
    return inferior1


##R008##
##20##
"""
Currificacion de la ley de la gravitacion universal.
"""
def cgravitacion(m1):
    def inferior1(m2):
        m1m2 = m1 * m2
        def inferior2(d):
            d2 = d ** 2
            return (G * m1m2) / d2
        return inferior2
    return inferior1


##R010##
##40##
"""
Procesar data con composicion por funciones de orden superior.
R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"
Salida: [3041, 30, 1000000, "28 de Julio"]
"""
def composicion_HOF(valor):
    def cadena(fun):
        if not fun:
            return valor
        return composicion_HOF(fun(valor))
    return cadena


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def fecha_texto(f):
    partes = f.split("/")                       # "28/07/2026" -> ["28","07","2026"]
    return partes[0] + " de " + meses[int(partes[1]) - 1]


fun0 = lambda st: st.split(",")

fun1 = lambda L: [int(e) if "/" not in e else e for e in L]


def fun2(L):
    _, A, *Z, Grande, Fecha = L
    return [A, sum(Z), Grande, Fecha]


fun3 = lambda L: [L[0], L[1], L[2], fecha_texto(L[3])]


##R011##
##10##
"""
Genera una lista de 100 numeros aleatorios y calcula su suma.
"""
def generaLista(N):
    if N == 0:
        return []
    return [random.randint(1, 100)] + generaLista(N - 1)


def sumaLista(L):
    if not L:
        return 0
    match L:
        case [P]:
            return P
        case [P, *F]:
            return P + sumaLista(F)


##R012##
##10##
"""
De una lista, genera dos listas: pares e impares.
"""
def pares_lista(L):
    if not L:
        return []
    match L:
        case [P]:
            if P % 2 == 0:
                return [P]
            return []
        case [P, *F]:
            if P % 2 == 0:
                return [P] + pares_lista(F)
            return pares_lista(F)


def impares_lista(L):
    if not L:
        return []
    match L:
        case [P]:
            if P % 2 != 0:
                return [P]
            return []
        case [P, *F]:
            if P % 2 != 0:
                return [P] + impares_lista(F)
            return impares_lista(F)
