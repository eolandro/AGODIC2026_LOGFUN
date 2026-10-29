from pathlib import Path
import statistics

RutaPython = Path(__file__).resolve()
RutaCSV    = RutaPython.parent / 'GanaGato.csv'

##R001##
##10##
"""
Del archivo GanaGato.csv abre el archivo en modo de solo lectura, agrega
comprobaciones para verificar la existencia del mismo.

Recomiendo el uso de la biblioteca Pathlib
"""
print("##R001##")

if not RutaCSV.exists():
    print("Archivo no encontrado!")
else:
    print("Archivo encontrado!")
    Archivo = RutaCSV.open("rt", encoding="utf-8")

    ##R002##
    ##10##
    """
    Del archivo GanaGato.csv, usando monads convierte y separa cada linea del
    archivo en una lista de listas
    """
    Archivo.readline()

    S0 = map(lambda st: st.strip(), Archivo)
    S1 = map(lambda st: st.split(','), S0)
    S2 = map(lambda iterable: [
                int(elemento) if '/' not in elemento else elemento
                for elemento in iterable
             ], S1)

    ListaDatos = list(S2)
    Archivo.close()

    print("\n##R002##")
    print(f"Total de registros: {len(ListaDatos)}")
    print(f"Ejemplo primer registro: {ListaDatos[0]}")

    ##R003##
    ##20##
    """
    Del ejercicio anterior, elimina todas las filas donde la BOLSA sea 0
    """
    S3 = filter(lambda registro: registro[-2] != 0, ListaDatos)
    ListaDatos = list(S3)

    print("\n##R003##")
    print(f"Registros con bolsa distinta de 0: {len(ListaDatos)}")

    ##R004##
    ##20##
    """
    Del ejercicio anterior, retira la columna NPRODUCTO
    """
    S4 = map(lambda registro: registro[1:], ListaDatos)
    ListaDatos = list(S4)

    print("\n##R004##")
    print(f"Ejemplo sin NPRODUCTO: {ListaDatos[0]}")

    ##R005##
    ##20##
    """
    Del ejercicio anterior, elimina todas las filas donde la fecha sea menor
    a 2010
    """
    def anioValido(registro):
        fecha = registro[-1]
        dia, mes, anio = fecha.split('/')
        return int(anio) >= 2010

    S5 = filter(anioValido, ListaDatos)
    ListaDatos = list(S5)

    print("\n##R005##")
    print(f"Registros desde 2010: {len(ListaDatos)}")

    ##R006##
    ##20##
    """
    Del ejercicio anterior, elimina todas las filas donde la suma de
    F1,F2,F3,F4,F5,F6,F7,F8 sea par
    """
    def sumaImpar(registro):
        Concurso, *Z, Mon, Fech = registro
        Cartas = Z
        return sum(Cartas) % 2 != 0

    S6 = filter(sumaImpar, ListaDatos)
    ListaDatos = list(S6)

    print("\n##R006##")
    print(f"Registros con suma impar: {len(ListaDatos)}")

    ##R007##
    ##25##
    """
    Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
    elimina todas las filas que tenga una tercia de ases (unos).
    """
    def tieneTerciaDe(valor):
        def filtroTercia(registro):
            Concurso, *Z, Mon, Fech = registro
            Cartas = Z
            Repeticiones = list(filter(lambda c: c == valor, Cartas))
            return len(Repeticiones) < 3
        return filtroTercia

    S7 = filter(tieneTerciaDe(1), ListaDatos)
    ListaDatosR007 = list(S7)

    print("\n##R007##")
    print(f"Registros sin tercia de ases: {len(ListaDatosR007)}")

    ##R008##
    ##30##
    """
    Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
    elimina todas las filas que tenga una tercia de Cincos.
    """
    S8 = filter(tieneTerciaDe(5), ListaDatos)
    ListaDatosR008 = list(S8)

    print("\n##R008##")
    print(f"Registros sin tercia de cincos: {len(ListaDatosR008)}")

    ##R009##
    ##30##
    """
    Del ejercicio ##R005, si F1,F2,F3,F4,F5,F6,F7,F8 fuesen cartas
    elimina todas las filas que tenga una dos pares.

    Nota 1,1,1,1; 2,2,2,2, 3,3,3,3; tambien entran como dos pares.
    """
    def contarPorValor(valor, Cartas):
        return len(list(filter(lambda c: c == valor, Cartas)))

    def tieneDosPares(registro):
        Concurso, *Z, Mon, Fech = registro
        Cartas = Z
        Conteos = map(lambda v: contarPorValor(v, Cartas), range(1, 6))
        Pares = list(filter(lambda n: n >= 2, Conteos))
        return len(Pares) < 2

    S9 = filter(tieneDosPares, ListaDatos)
    ListaDatosR009 = list(S9)

    print("\n##R009##")
    print(f"Registros sin dos pares: {len(ListaDatosR009)}")

    ##R010##
    ##10##
    """
    Del ejercicio ##R005, calcula la bolsa minima.
    """
    RegistroBolsaMinima = min(ListaDatos, key=lambda r: r[-2])

    print("\n##R010##")
    print(f"Bolsa minima: {RegistroBolsaMinima[-2]}")
    print(f"Registro: {RegistroBolsaMinima}")


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
print("\n##R011##")

def compoGen(valor):
    Terminado = False
    Resultado = valor
    while not Terminado:
        funcion = yield Resultado
        if funcion is None:
            Terminado = True
            continue
        Resultado = funcion(Resultado)
    yield Resultado

MESES = {
    "01": "Enero",   "02": "Febrero", "03": "Marzo",
    "04": "Abril",   "05": "Mayo",    "06": "Junio",
    "07": "Julio",   "08": "Agosto",  "09": "Septiembre",
    "10": "Octubre", "11": "Noviembre", "12": "Diciembre",
}

def fun0(st):
    return st.strip()

def fun1(st):
    return st.split(',')

def fun2(lista):
    return [
        int(elemento) if '/' not in elemento else elemento
        for elemento in lista
    ]

def fun3(lista):
    NProducto, Concurso, *Z, Mon, Fech = lista
    SumaCartas = sum(Z)
    Dia, Mes, Anio = Fech.split('/')
    FechaTexto = f"{Dia} de {MESES[Mes]}"
    return [Concurso, SumaCartas, Mon, FechaTexto]

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
"""
print("\n##R012##")

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
        n = n + 1

g = gBadaBoom()
L = [next(g) for a in range(10)]
print(L)
