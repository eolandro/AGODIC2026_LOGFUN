#--------------------------------------------------------------------------------------
#   #R001##
#   #10##
#--------------------------------------------------------------------------------------
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""
from pathlib import Path

ruta = Path("GanaGato.csv")

if ruta.exists() and ruta.is_file():
    Archivo = open(ruta, "r")
    print("El archivo si existe en la ruta especificada")
else:
    print("Error: El archivo no existe en la ruta especificada.")
#--------------------------------------------------------------------------------------
#   #R002##
#   #10##
#--------------------------------------------------------------------------------------
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""
Archivo.readline()

S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)
#--------------------------------------------------------------------------------------
#   #R003##
#   #20##
#--------------------------------------------------------------------------------------
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""
S2 = map(lambda iterable: [int(elemento) if not '/' in elemento else elemento for elemento in iterable], S1)
S3 = filter(lambda fila: fila[-2] != 0, S2)
#--------------------------------------------------------------------------------------
#   #R004##
#   #20##
#--------------------------------------------------------------------------------------
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""
S4 = map(lambda reg: reg[1:], S3)
#--------------------------------------------------------------------------------------
#   #R005##
#   #20##
#--------------------------------------------------------------------------------------
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""
S5 = filter(lambda fila: int(fila[-1].split('/')[2]) >= 2010, S4)

Lista_R005 = list(S5)
Archivo.close()
#--------------------------------------------------------------------------------------
#   #R006##
#   #20##
#--------------------------------------------------------------------------------------
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""
S6 = filter(lambda fila: sum(fila[1:9]) % 2 != 0, Lista_R005)
Lista_R006 = list(S6)
#--------------------------------------------------------------------------------------
#   #R007##
#   #25##
#--------------------------------------------------------------------------------------
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
S7 = filter(lambda fila: fila[1:9].count(1) < 3, Lista_R005)
Lista_R007 = list(S7)
#--------------------------------------------------------------------------------------
#   #R008##
#   #30##
#--------------------------------------------------------------------------------------
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""
S8 = filter(lambda fila: fila[1:9].count(5) < 3, Lista_R005)
Lista_R008 = list(S8)
#--------------------------------------------------------------------------------------
#   #R009##
#   #30##
#--------------------------------------------------------------------------------------
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una dos pares.

Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.
"""
def conteo_pares(cartas):
    return sum(cartas.count(num) // 2 for num in range(1, 6))

S9 = filter(lambda fila: conteo_pares(fila[1:9]) < 2, Lista_R005)
Lista_R009 = list(S9)
#--------------------------------------------------------------------------------------
#   #R010##
#   #10##
#--------------------------------------------------------------------------------------
"""
Del ejercicio ##R005, calcula la bolsa minima.
"""
bolsa_min = min(Lista_R005, key=lambda fila: fila[9])[9]
#--------------------------------------------------------------------------------------
#   #R011##
#   #40##
#--------------------------------------------------------------------------------------
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
    fun = yield
    while fun is not None:
        valor = fun(valor)
        fun = yield
    yield valor 

fun0 = lambda st: [int(x) if x.isdigit() else x for x in st.split(',')]

def fun1(lista):
    return [lista[1], sum(lista[2:10]), lista[10], lista[11]]

def fun2(lista):
    meses = {"01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril", "05":"Mayo", 
             "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre", 
             "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}
    dia, mes, _ = lista[3].split('/')
    lista[3] = f"{int(dia)} de {meses[mes]}"
    return lista

R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = compoGen(R)
T.send(None)
T.send(fun0)
T.send(fun1)
T.send(fun2)
R = T.send(None)

print(R)
#--------------------------------------------------------------------------------------
#   #R012##
#   #20##
#--------------------------------------------------------------------------------------
"""
Badaboom! con generadores, realizar un generador infinito que retorne numeros
positivos, uno a uno bajo las siguientes reglas.

Si un numero es multiplo de 3 y 5 retorna "BadaBoom!"
Si un numero es multiplo de 3 retorna "Bada"
Si un numero es multiplo de 5 retorna "Boom!"
Si no caen en las reglas anteriores retorna el numero
"""
def gBadaBoom():
    n = 1
    while True:
        if n % 3 == 0 and n % 5 == 0:
            yield "BadaBoom!"
        elif n % 3 == 0:
            yield "Bada"
        elif n % 5 == 0:
            yield "Boom!"
        else:
            yield n
        n += 1

g = gBadaBoom()
L = [next(g) for a in range(10)]
print(L)