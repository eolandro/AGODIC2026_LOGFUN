##R001##
##10##
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""
print("")
print("##R001##")
from pathlib import Path

Ruta = Path('GanaGato.csv')

Archivo = open(Ruta, 'r', encoding='utf-8')
print('El archivo', Ruta.name, 'Esta Abierto')
print(Archivo.readline())
#Archivo.close()


##R002##
##10##
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""
print("")
print("##R002##")

Limite = 5

def composicion(valor):
	print(valor)
	def cadena(fun):
		if not fun:
			return valor
		return composicion(fun(valor))
	return cadena

def procesarLinea(SL):
	F = composicion(SL)
	F = F(lambda st : st.strip())
	F = F(lambda st : st.split(','))
	F = F(lambda iterable : [
		int(elemento) if not '/' in elemento else elemento
		for elemento in iterable
	])
	return F(None)
	
Lineas = [linea for linea in Archivo]
ListaDeListas = [procesarLinea(linea) for linea in Lineas[1:Limite + 1]]
print(ListaDeListas)

##R003##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""
print("")
print("##R003##")
#ListaDeListas = [procesarLinea(linea) for linea in Lineas[1:]]
SinCero = list(filter(lambda reg: reg[-2] != 0, ListaDeListas))
Eliminadas = [reg for reg in ListaDeListas if reg[-2] == 0]
print('Filas de eliminadas:', Eliminadas[:3])

##R004##
##20##
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""
print("")
print("##R004##")
SinNProducto = [reg[1:] for reg in SinCero]
print(SinNProducto[:2])


##R005##
##20##
print("")
print("##R005##")
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""

def meses_pares(registro):
	fecha = registro[-1]
	dia,mes,año = fecha.split('/')
	return int(año) < 2010
	
Eliminadas = [reg for reg in SinNProducto if meses_pares(reg)]
print('Fechas de eliminadas:', Eliminadas[:3])

##R006##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""
print("")
print("##R006##")

def limpiar(lista):
	Q2, *Z,MON,FECH = lista
	return sum(Z) % 2 == 1

EliminarPares = [reg for reg in Eliminadas if limpiar(reg)]
print('Sumas de eliminadas:', [sum(reg[1:-2]) for reg in Eliminadas[:5]])

##R007##
##25##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
##R008##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""
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
print("")
print("##R010##")
Registro = min(Eliminadas, key = lambda r: r[-2])
Bolsaminima = Registro[-2]

print('La bolsa minima es:', Bolsaminima)

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
