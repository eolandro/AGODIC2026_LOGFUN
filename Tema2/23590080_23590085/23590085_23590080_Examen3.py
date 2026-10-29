print("Guillermo Daniel Lopez Garcia")
print("Leonardo Emmanuel Buendia Ramos")
print("\n")
##R001##
##10##
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""

print("#--------------##R001##--------------#\n")


from pathlib import Path
Archivo = Path('GanaGato.csv')

if Archivo.exists():
	Archivo = open('GanaGato.csv', 'r')
	Archivo.readline()
	print("Archivo abierto correctamente")
	#Dejamos el archivo abierto para los demas reactivos y no abrirlo de nuevo en cada reactivo

else:
	print("El archivo no existe")

print("\n")

##R002##
##10##
"""
Del archivo GanaGato.csv, usando monads convierte  y separa cada linea del 
archivo en una lista de listas
"""

print("#--------------##R002##--------------#\n")

#Quitamos la primera linea que es el encabezado
S0 = map(lambda st: st.strip(), Archivo)

#Separamos cada linea por comas y creamos una lista de elementos
S1 = map(lambda st: st.split(','), S0)
#Guardamos el resultado (lista de elementos) en una lista

ListaDatos002 = list(S1)

#Mostramos los primeros 10 elementos de la lista de listas
print(ListaDatos002[:5])


print("\n")

##R003##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
"""
print("#--------------##R003##--------------#\n")


#Filtramos la lista y comprobamos que la posicion -2 no se igual a 0
S2 = filter(lambda e: e[-2] != '0', ListaDatos002)

ListaDatos003 = list(S2)
print(ListaDatos003[:5])


print("\n")


##R004##
##20##
"""
Del ejercicio anterior, retira la columna NPRODUCTO
"""
print("#--------------##R004##--------------#\n")

#Usando la lista anterior la recorremos apartir de los elementos en la posicion 2[1] eliminando la primera columna[0]
S3 = map(lambda e: e[1:], ListaDatos003)

ListaDatos004 = list(S3)
print(ListaDatos004[:5])


print("\n")

##R005##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
a 2010
"""

print("#--------------##R005##--------------#\n")


#Usamos el resultado anterior para quitar todos los elementos que sean de fecha menor al 2010
S4 = filter(lambda e: int(e[-1][-4:]) >= 2010, ListaDatos004)

ListaDatos005 = list(S4)
print(ListaDatos005[:5])

print("\n")


##R006##
##20##
"""
Del ejercicio anterior, elimina todas las filas donde la suma de
F1,F2,F3,F4,F5,F6,F7,F8 sea par
"""
print("#--------------##R006##--------------#\n")

#Suma de filas y comprobacion de par
S5 = filter(lambda e: sum(int(f) for f in e[1:9]) % 2 != 0, ListaDatos005)

ListaDatos006 = list(S5)
print(ListaDatos006[:5])


print("\n")


##R007##
##25##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de ases (unos).
"""
print("#--------------##R007##--------------#\n")

#filtro para eliminar las filas que tengan una tercia de ases (unos)
S6 = filter(lambda e: sum(int(f) == 1 for f in e[1:9]) < 3, ListaDatos005)

ListaDatos007 = (S6)
print(ListaDatos006[:5])


##R008##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una tercia de Cincos.
"""

print("#--------------##R008##--------------#\n")

#filtro para eliminar las filas que tengan una tercia de Cincos
S7 = filter(lambda e: sum(int(f) == 5 for f in e[1:9]) < 3, ListaDatos005)

ListaDatos007 = list(S7)
print(ListaDatos007[:5])


print("\n")


##R009##
##30##
"""
Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
elimina todas las filas que tenga una dos pares.

Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.

"""

print("#--------------##R009##--------------#\n")

#filtro para eliminar las filas que tengan dos pares
S8 = filter(lambda e: sum([sum(int(f) == i for f in e[1:9]) // 2 for i in range(1, 6)]) < 2, ListaDatos005)

ListaDatos008 = list(S8)
print(ListaDatos008[:5])


print("\n")


##R010##
##10##
"""
Del ejercicio ##R005, calcula la bolsa minima.

"""

print("#--------------##R010##--------------#\n")

S9 = min(ListaDatos005, key=lambda e: int(e[-2]))

print("La bolsa mas baja fue: ")
print(S9)

print("\n")


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
print("#--------------##R011##--------------#\n")

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

def fun0(valor):
    return valor.strip()

def fun1(valor):
    return valor.split(',')

def fun2(valor):
    return [int(elemento) if not '/' in elemento else elemento for elemento in valor]

def fun3(lista):
    Q1, Q2, *Z, MON, FECH = lista
    dia, mes, anio = FECH.split('/')
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril',
             'Mayo', 'Junio', 'Julio', 'Agosto',
             'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    fecha = dia + " de " + meses[int(mes)-1]
    return [Q2, sum(Z), MON, fecha]


R = "20,3041,5,2,4,1,5,3,5,5,1000000,28/07/2026"
T = compoGen(R)
T.send(None)
T.send(fun0)
T.send(fun1)
T.send(fun2)
T.send(fun3)
R = T.send(None)
print(R)

print("\n")
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

print("#--------------##R011##--------------#\n")

def gBadaBoom():
	num = 1
	while True:
		if num % 3 == 0 and num % 5 == 0:
			yield "BadaBoom!"
		elif num % 3 == 0:
			yield "Bada"
		elif num % 5 == 0:
			yield "Boom!"
		else:
			yield num
		num = num + 1

g = gBadaBoom()
L = [next(g) for a in range(15)]
print(L)

print("\n")
print("Guillermo Daniel Lopez Garcia")
print("Leonardo Emmanuel Buendia Ramos")