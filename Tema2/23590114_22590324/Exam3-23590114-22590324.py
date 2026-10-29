#Oliver Uriel Pagola Perez 23590114
#Javier Yael Enriquez Martinez 22590324
from pathlib import Path

##R001##
##10##
if not Path('GanaGato.csv').exists():
    raise FileNotFoundError("El archivo GanaGato.csv no existe.")

Archivo = open('GanaGato.csv')
Archivo.readline()

##R002##
##10##
S0 = map(lambda st: st.strip(), Archivo)
S1 = map(lambda st: st.split(','), S0)
S2 = map(lambda iterable: [
    int(elemento) if not '/' in elemento else elemento
    for elemento in iterable
], S1)

##R003##
##20##
S3 = filter(lambda reg: int(reg[10]) != 0, S2)

##R004##
##20##
S4 = map(lambda reg: reg[1:], S3)

##R005##
##20##
def año_valido(reg):
    fecha = reg[10]
    dia, mes, año = fecha.split('/')
    return int(año) >= 2010

S5 = filter(año_valido, S4)

##R006##
##20##
S6 = filter(lambda reg: sum(reg[1:9]) % 2 != 0, S5)

##R010##
##10##
ListaDatos = list(S5)
Archivo.close()

if ListaDatos:
    bolsa_min = min(ListaDatos, key=lambda r: int(r[9]))[9]
    print("La bolsa minima es: " + str(bolsa_min))
else:
    print("La lista final esta vacia tras los filtros.")

#--------------------------------------------------------------
##R012##
##20##
def gBadaBoom():
    N = 1
    while True:
        match (N % 3, N % 5):
            case (0, 0):
                yield "BadaBoom!"
            case (0, _):
                yield "Bada"
            case (_, 0):
                yield "Boom!"
            case _:
                yield N
        N += 1

g = gBadaBoom()
L = [next(g) for a in range(67)]
print(L)