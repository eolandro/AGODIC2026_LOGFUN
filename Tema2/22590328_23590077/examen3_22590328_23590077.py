#R001##
##10##
print("######################## - EJERCICIO 1 - #########################################")

"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""


from pathlib import Path

ruta = Path('GanaGato.csv')

if not ruta.exists():
    print(f"(!)Error(!): El archivo '{ruta}' no existe dentro de la misma carpeta <-")
elif not ruta.is_file():
    print(f"(!)Error(!): El archivo que se lee es una carpeta con el mismo nombre... <-")
else:
    try:
        with ruta.open(mode='r') as archivo:
            contenido = archivo.read()
            print("Archivo abierto!")
            #print(contenido)
    except PermissionError:
         print(f"(!)Error(!): No se tiene permiso para leer '{ruta}' <-")


print("######################## - EJERCICIO 2 - #########################################")
##R002##
##10##
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""

archivo = open('GanaGato.csv')
archivo.readline()
S0 = map(lambda st : st.strip(),archivo)
S1 = map(lambda st : st.split(','), S0)
#A = list(S1)
#print(A)
# canario de cuantos registros son : 3080
#print(len(A))

print("######################## - EJERCICIO 3 - #########################################")
##R003##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""
S2 = map(lambda iterable : [
        int(elemento) if not '/' in elemento else elemento
        for elemento in iterable
        ], S1)
S3 = filter(lambda iterable: iterable[-2] >  0 ,S2)

#A = list(S3)
#print(A)
# canario de cuantos registros son : 3074
#print(len(A))

print("######################## - EJERCICIO 4 - #########################################")
##R004##
##20##
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""
S4 = map(lambda reg: reg[1:] ,S3)

#A = list(S4)
#print(A)
# canario de cuantos registros son : 3074
#print(len(A))

print("######################## - EJERCICIO 5 - #########################################")
##R005##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""
def meses_bef2010(registro):
        fecha = registro[-1]
        dia,mes,año = fecha.split('/')
        return int(año) >= 2010

S5 = filter(meses_bef2010 ,S4)

A = list(S5)
print(A)
# canario de cuantos registros son : 2582
print(len(A))



print("######################## - EJERCICIO 6 - #########################################")
##R006##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""


def elim_filpar(registro):
     Fs = registro[1:9]
     return sum(Fs) % 2 != 0


S6 = filter(elim_filpar,A)
A1 = list(S6)
#print(A1)
# canario de cuantos registros son : 1291
#print(len(A1))

# NOTA: Anteriormente se trabajo con S5 para cada uno de los siguientes ejercicios,
    #   pero se opto por convertir el S5 en A, para poder correrlo en todos los
    #   ejercicios siguientes a la par, aunque no se puede observar correctamente en
    #   terminal porque son muchos registros...


print("######################## - EJERCICIO 7 - #########################################")
##R007##
##25##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
def sin_tercia_ases(registro):
    mano = registro[1:9]
    return mano.count(1) != 3

S7 = filter(sin_tercia_ases, A)
A2 = list(S7)
#print(A2)
# canario de cuantos registros son : 2200
#print(len(A2))






print("######################## - EJERCICIO 8 - #########################################")
##R008##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""
def sin_tercia_cincos(registro):
    cartas = registro[1:9]
    return cartas.count(5) != 3

S8 = filter(sin_tercia_cincos, A)
A3 = list(S8)
#print(A3)
# canario de cuantos registros son : 2249
#print(len(A3))




print("######################## - EJERCICIO 9 - #########################################")
##R009##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una dos pares.

Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.

"""
def sin_dos_pares(registro):
    cartas = registro[1:9]
    pares = sum(cartas.count(v) // 2 for v in set(cartas))
    return pares != 2

S9 = filter(sin_dos_pares, A)
A4 = list(S9)
#print(A4)
# canario de cuantos registros son : 1792
#print(len(A4))

print("######################## - EJERCICIO 10 - #########################################")
##R010##
##10##
"""
Del ejercicio ##R005, calcula la bolsa minima.

"""

print('La bolsa minima, fue : ')
print(min(A,key = lambda r: r[-2])[-2])

print("Archivo cerrado!")
archivo.close()


print("######################## - EJERCICIO 11 - #########################################")
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


MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def fun0(texto):
    return texto.strip().split(',')


def fun1(campos):
    return [int(c) if '/' not in c else c for c in campos]


def fun2(registro):
    return registro[1:]


def fun3(registro):
    concurso, *F, bolsa, fecha = registro
    return [concurso, sum(F), bolsa, fecha]


def fun4(registro):
    concurso, suma, bolsa, fecha = registro
    dia, mes, anio = fecha.split('/')
    return [concurso, suma, bolsa, f"{int(dia)} de {MESES[int(mes) - 1]}"]


R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"

T = compoGen(R)
T.send(None)
T.send(fun0)
T.send(fun1)
T.send(fun2)
T.send(fun3)
T.send(fun4)
R = T.send(None)
print(R)




print("######################## - EJERCICIO 12 - #########################################")
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
    n = 1
    while True:
        if n % 15 == 0:
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