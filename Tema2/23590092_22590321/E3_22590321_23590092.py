##R001##
##10##
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""

from pathlib import Path

archivo = Path('GanaGato.csv')

if archivo.exists():
    Archivo = open('GanaGato.csv', 'r')
    print("El archivo existe y se abrió correctamente")
    Archivo.close()
else:
    print("El archivo no existe")

##R002##
##10##
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""

Archivo = open('GanaGato.csv')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

datos = list(S1)

print(datos[:3])
Archivo.close()

##R003##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""

Archivo = open('GanaGato.csv')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

S2 = list(S1)

S3 = filter(lambda registro: int(registro[10]) != 0, S2)

Resultado = list(S3)

print(Resultado[:5])

Archivo.close()

##R004##
##20##
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""

Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Preparar los datos del R003
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

Archivo.close()

# Eliminar la primera columna
S4 = map(lambda registro: registro[1:], Resultado)
Resultado4 = list(S4)

print(Resultado4[:5])


##R005##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""

Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Preparar los datos del R003
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

# Preparar los datos del R004
S4 = map(lambda registro: registro[1:], Resultado)
Resultado4 = list(S4)

Archivo.close()

# Conservar registros del año 2010 en adelante
S5 = filter(
    lambda registro: int(registro[10].split('/')[-1]) >= 2010,
    Resultado4
)

Resultado5 = list(S5)

print(Resultado5[:5])


##R006##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""

Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Datos del R003
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

# Datos del R004
S4 = map(lambda registro: registro[1:], Resultado)
Resultado4 = list(S4)

Archivo.close()

# Datos del R005
S5 = filter(
    lambda registro: int(registro[10].split('/')[-1]) >= 2010,
    Resultado4
)
Resultado5 = list(S5)

# R006: conservar solo registros cuya suma sea impar
S6 = filter(
    lambda registro: sum(map(int, registro[1:9])) % 2 != 0,
    Resultado5
)

Resultado6 = list(S6)

print(Resultado6[:5])

##R007##
##25##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Datos del R003: eliminar filas donde BOLSA sea 0
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

# Datos del R004: retirar la columna NPRODUCTO
S3 = map(lambda registro: registro[1:], Resultado)
Resultado3 = list(S3)

Archivo.close()

# Datos del R005: conservar registros del año 2010 en adelante
S4 = filter(
    lambda registro: int(registro[10].split('/')[-1]) >= 2010,
    Resultado3
)
Resultado4 = list(S4)

# R007: eliminar filas que tengan tres o más unos
S5 = filter(
    lambda registro: registro[1:9].count('1') < 3,
    Resultado4
)

Resultado5 = list(S5)

print(Resultado5[:5])

##R008##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""
Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Datos del R003
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

# Datos del R004
S3 = map(lambda registro: registro[1:], Resultado)
Resultado3 = list(S3)

Archivo.close()

# Datos del R005
S4 = filter(
    lambda registro: int(registro[10].split('/')[-1]) >= 2010,
    Resultado3
)
Resultado4 = list(S4)

# R008: eliminar filas que tengan tres o más cincos
S5 = filter(
    lambda registro: registro[1:9].count('5') < 3,
    Resultado4
)

Resultado5 = list(S5)

print(Resultado5[:5])

##R009##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una dos pares.

Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.

"""
Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Datos del R003
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

# Datos del R004
S3 = map(lambda registro: registro[1:], Resultado)
Resultado3 = list(S3)

Archivo.close()

# Datos del R005
S4 = filter(
    lambda registro: int(registro[10].split('/')[-1]) >= 2010,
    Resultado3
)
Resultado4 = list(S4)

# R009: eliminar filas que tengan dos pares o más
S5 = filter(
    lambda registro: sum(
        map(
            lambda carta: registro[1:9].count(carta) // 2,
            registro[1:9]
        )
    ) < 4,
    Resultado4
)

Resultado5 = list(S5)

print(Resultado5[:5])

##R010##
##10##
"""
Del ejercicio ##R005, calcula la bolsa minima.

"""
Archivo = open('GanaGato.csv', 'r')
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)

# Datos del R003
S2 = filter(lambda registro: int(registro[10]) != 0, S1)
Resultado = list(S2)

# Datos del R004
S3 = map(lambda registro: registro[1:], Resultado)
Resultado3 = list(S3)

Archivo.close()

# Datos del R005
S4 = filter(
    lambda registro: int(registro[10].split('/')[-1]) >= 2010,
    Resultado3
)
Resultado4 = list(S4)

# R010: calcular la bolsa mínima
S5 = map(lambda registro: int(registro[9]), Resultado4)

Resultado5 = list(S5)

print(min(Resultado5))

##R011##
##40##
"""
Procesar data

Utilizando el patron de diseño composicion con generadores
obten la salida correspondiente:

R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = compoGen(R)
T.send(None)
T.send(fun0)
T.send(fun1)
T.send(fun2)
T.send(fun3) #...
R = T.send(None)
print(R)
# [3041,30,1000000,"28 de Julio"]

"""
def compoGen(valor):
    Terminado = False
    Resultado = valor

    while not Terminado:
        funcion = yield Resultado

        if funcion == None:
            Terminado = True
            continue

        Resultado = funcion(Resultado)

    yield Resultado


def fun0(R):
    S0 = R.split(',')

    S1 = [
        int(elemento) if not '/' in elemento else elemento
        for elemento in S0
    ]

    return S1


def fun1(R):
    return [R[1], R[2:10], R[10], R[11]]


def fun2(R):
    return [R[0], sum(R[1]), R[2], R[3]]


def fun3(R):
    fecha = R[3].split('/')
    R[3] = fecha[0] + " de Julio"
    return R


R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = compoGen(R)

T.send(None)
T.send(fun0)
T.send(fun1)
T.send(fun2)
T.send(fun3)

R = T.send(None)

print(R)

##R012##
##20##
"""
Badaboom! con generadores, realizar un generador infinito que retorne numeros
positivos, uno a uno bajo las siguientes reglas.

Si un numero es multiplo de 3 y 5 retorna "BadaBoom!"
Si un numero es multiplo de 3 retorna "Bada"
Si un numero es multiplo de 5 retorna "Boom!"
Si no caen en las reglas anteriores retorna el numero

def gBadaBoom():
	pass

g = gBadaBoom()
L = [next(g) for a in range(10)]
print(L)
# [1,2,"Bada",4,"Boom!",6,7,8,9,10]
"""
def gBadaBoom():
    N = 1

    while True:
        if N % 3 == 0 and N % 5 == 0:
            yield "BadaBoom!"
        elif N % 3 == 0:
            yield "Bada"
        elif N % 5 == 0:
            yield "Boom!"
        else:
            yield N

        N = N + 1


g = gBadaBoom()

L = [next(g) for a in range(10)]

print(L)
