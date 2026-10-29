##R001##
##10##
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""
from pathlib import Path
import sys

sys.setrecursionlimit(10000)

archivo = Path(__file__).with_name("GanaGato1.csv")
if archivo.exists() and archivo.is_file():
	f = open(archivo, "r")
	lineas = f.readlines()
	f.close()
	print("R001: archivo encontrado y abierto en modo de lectura")
else:
	lineas = []
	print("R001: no se encontro GanaGato1.csv")
##R002##
##10##
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""
def monad_separar(L):
	if not L:
		return
	match L:
		case [P]:
			yield list(map(
				lambda elemento: int(elemento) if "/" not in elemento else elemento,
				P.strip().split(",")
			))
		case [P, *F]:
			yield list(map(
				lambda elemento: int(elemento) if "/" not in elemento else elemento,
				P.strip().split(",")
			))
			for registro in monad_separar(F):
				yield registro


R002 = list(monad_separar(lineas[1:]))
print(f"R002: {len(R002)} registros; ejemplo: {R002[0] if R002 else []}")
##R003##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""
R003 = list(filter(lambda registro: int(registro[10]) != 0, R002))
print(f"R003: {len(R003)} registros")
##R004##
##20##
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""
R004 = list(map(lambda registro: registro[1:], R003))
print(f"R004: {len(R004)} registros; primera fila: {R004[0] if R004 else []}")
##R005##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""
def año_registro(registro):
	return int(registro[10].split("/")[2])


R005 = list(filter(lambda registro: año_registro(registro) >= 2010, R004))
print(f"R005: {len(R005)} registros")
##R006##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""
def suma_cartas(registro):
	return sum(registro[1:9])


R006 = list(filter(lambda registro: suma_cartas(registro) % 2 != 0, R005))
print(f"R006: {len(R006)} registros")
##R007##
##25##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
R007 = list(filter(lambda registro: registro[1:9].count(1) < 3, R005))
print(f"R007: {len(R007)} registros")
##R008##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""
R008 = list(filter(lambda registro: registro[1:9].count(5) < 3, R005))
print(f"R008: {len(R008)} registros")
##R009##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una dos pares.

Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.

"""
def tiene_dos_pares(registro):
	cartas = registro[1:9]
	return sum(cartas.count(carta) // 2 for carta in set(cartas)) >= 2


R009 = list(filter(lambda registro: not tiene_dos_pares(registro), R005))
print(f"R009: {len(R009)} registros")
##R010##
##10##
"""
Del ejercicio ##R005, calcula la bolsa minima.

"""
R010 = min(R005, key=lambda registro: int(registro[9])) if R005 else None
print(f"R010: bolsa minima = {R010[9] if R010 else 'sin registros'}")
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
	funcion = yield
	while funcion is not None:
		valor = funcion(valor)
		funcion = yield
	yield valor


def fun0(cadena):
	return cadena.split(",")


def fun1(registro):
	datos = [int(elemento) for elemento in registro[:-1]]
	return datos[1:] + [registro[-1]]


def fun2(registro):
	return [registro[0], sum(registro[1:9]), registro[9], registro[10]]


def fun3(registro):
	meses = [
		"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
		"Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
	]
	dia, mes, _ = registro[3].split("/")
	return [registro[0], registro[1], registro[2], f"{int(dia)} de {meses[int(mes) - 1]}"]


R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"
T = compoGen(R)
T.send(None)
T.send(fun0)
T.send(fun1)
T.send(fun2)
T.send(fun3)
R = T.send(None)
print("R011:", R)
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
# [1,2,"Bada",4,"Boom!","Bada",7,8,"Bada","Boom!"]
"""
def gBadaBoom():
	numero = 1
	while True:
		if numero % 15 == 0:
			yield "BadaBoom!"
		elif numero % 3 == 0:
			yield "Bada"
		elif numero % 5 == 0:
			yield "Boom!"
		else:
			yield numero
		numero += 1


g = gBadaBoom()
L = [next(g) for a in range(10)]
print("R012:", L)
