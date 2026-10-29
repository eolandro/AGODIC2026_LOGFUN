print("Examen 3 del tema 2")

from pathlib import Path
#Composicion
def composicion(valor):
    def cadena(fun):
        if not fun:
            return valor
        return composicion(fun(valor))
    return cadena
##R001##
##10##
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""

ruta = Path(__file__).resolve().parent / 'GanaGato.csv' 
if not ruta.exists():
    raise FileNotFoundError('No existe la ruta ',ruta)
if not ruta.is_file():
    raise ValueError(ruta,' No es un archivo')
with ruta.open('r') as archivo:
    lineas = archivo.readlines()[1:] 

print("\nR001")
print('Ruta:', ruta)
print('El archivo existe:', ruta.is_file())

##R002##
##10##
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""
def a_valor(x):
    return x if '/' in x else int(x)
 
R2 = (composicion(lineas)
      (lambda L: [s.strip() for s in L])
      (lambda L: [s.split(',') for s in L])
      (lambda L: [[a_valor(e) for e in fila] for fila in L])
      (None))
print("\nR002")
print('Numero de filas:', len(R2))
print('Primera fila:', R2[0])
print('Última fila:', R2[-1])
##R003##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""
R3 = list(filter(lambda r: r[10] != 0, R2))
print("\nR003")
print('Se eliminaron', len(R2) - len(R3),'lineas')
print('Filas antes/después:', len(R2), '/', len(R3))

##R004##
##20##
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""
R4 = [r[1:] for r in R3]

print("\nR004")
print('Prueba :', R4[0])
##R005##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""
def año_filtrar(r):
    return int(r[-1].split('/')[2])
R5 = list(filter(lambda r: año_filtrar(r) >= 2010, R4))

print("\nR005")
print('Filas antes/después:', len(R4), '/', len(R5))
print('Año mínimo   :', min(año_filtrar(r) for r in R5))
print('Primera fila :', R5[0])
print('Última fila  :', R5[-1])
##R006##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""
R6 = list(filter(lambda r: sum(r[1:9]) % 2 != 0, R5))

print("\nR006")
print('Filas antes/después:', len(R5), '/', len(R6))
print('Quedan', sum(1 for r in R6 if sum(r[1:9]) % 2 == 0),'filas con suma par')
print('Ejemplo      :', R6[0], '-> suma =', sum(R6[0][1:9]))
print('Ejemplo      :', R6[-1], '-> suma =', sum(R6[0][1:9]))

##R007##
##25##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
R7 = list(filter(lambda r: r[1:9].count(1) < 3, R5))

print("\nR007")
print('Filas antes/después:', len(R5), '/', len(R7))
print('Primera fila :', R7[0])
print('Última fila  :', R7[-1])
##R008##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""
R8 = list(filter(lambda r: r[1:9].count(5) < 3, R5))

print("\nR008")
print('Filas antes/después:', len(R5), '/', len(R8))
print('Primera fila :', R8[0])
print('Última fila  :', R8[-1])
##R009##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una dos pares.

Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.

"""

##R010##
##10##
"""
Del ejercicio ##R005, calcula la bolsa minima.

"""
R10 = min(R5, key=lambda r: r[9])[9]

print("\nR010")
print('La bolsa minima es de: ', R10)

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
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield "BadaBoom!"
        elif i % 3 == 0:
            yield "Bada"
        elif i % 5 == 0:
            yield "Boom!"
        else:
            yield i
        i += 1

print("\nR012")
g = gBadaBoom()
L = [next(g) for a in range(10)]
print(L)

