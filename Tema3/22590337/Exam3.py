##R001##
##50##
progenitor = [
    ("monsieur_delacour", "fleur"),
    ("apolline_delacour", "fleur"),
    ("monsieur_delacour", "gabrielle"),
    ("apolline_delacour", "gabrielle"),
    ("arthur", "bill"),
    ("molly", "bill"),
    ("arthur", "charlie"),
    ("molly", "charlie"),
    ("arthur", "percy"),
    ("molly", "percy"),
    ("arthur", "fred"),
    ("molly", "fred"),
    ("arthur", "george"),
    ("molly", "george"),
    ("arthur", "ron"),
    ("molly", "ron"),
    ("arthur", "ginny"),
    ("molly", "ginny"),
    ("bill", "victoire"),
    ("fleur", "victoire"),
    ("bill", "dominique"),
    ("fleur", "dominique"),
    ("bill", "louis"),
    ("fleur", "louis"),
    ("percy", "molly_ii"),
    ("audrey", "molly_ii"),
    ("percy", "lucy"),
    ("audrey", "lucy"),
    ("george", "fred_ii"),
    ("angelina", "fred_ii"),
    ("george", "roxanne"),
    ("angelina", "roxanne"),
    ("ron", "rose"),
    ("hermione", "rose"),
    ("ron", "hugo"),
    ("hermione", "hugo"),
    ("harry", "james_sirius"),
    ("ginny", "james_sirius"),
    ("harry", "albus_severus"),
    ("ginny", "albus_severus"),
    ("harry", "lily_luna"),
    ("ginny", "lily_luna"),
    ("james_potter", "harry"),
    ("lily_evans", "harry"),
    ("vernon_dursley", "dudley"),
    ("petunia_evans", "dudley"),
    ("pollux_black", "cygnus_black_iii"),
    ("pollux_black", "walburga_black"),
    ("cygnus_black_iii", "bellatrix"),
    ("druella_rosier", "bellatrix"),
    ("cygnus_black_iii", "andromeda"),
    ("druella_rosier", "andromeda"),
    ("cygnus_black_iii", "narcissa"),
    ("druella_rosier", "narcissa"),
    ("orion_black", "sirius_black"),
    ("walburga_black", "sirius_black"),
    ("orion_black", "regulus_black"),
    ("walburga_black", "regulus_black"),
    ("andromeda", "nymphadora_tonks"),
    ("ted_tonks", "nymphadora_tonks"),
    ("nymphadora_tonks", "teddy_lupin"),
    ("remus_lupin", "teddy_lupin"),
    ("narcissa", "draco"),
    ("lucius_malfoy", "draco"),
    ("draco", "scorpius"),
    ("astoria_greengrass", "scorpius"),
    ("xenophilius_lovegood", "luna"),
    ("lunas_mum", "luna"),
    ("luna", "lysander"),
    ("rolf_scamander", "lysander"),
    ("luna", "lorcan"),
    ("rolf_scamander", "lorcan"),
    ("mr_longbottom", "frank"),
    ("augusta", "frank"),
    ("frank", "neville"),
    ("alice", "neville"),
]

hombre = [
    "monsieur_delacour", "arthur", "bill", "charlie", "percy", "fred",
    "george", "ron", "louis", "fred_ii", "hugo", "james_potter", "harry",
    "james_sirius", "albus_severus", "vernon_dursley", "dudley",
    "pollux_black", "cygnus_black_iii", "orion_black", "sirius_black",
    "regulus_black", "rodolphus_lestrange", "ted_tonks", "remus_lupin",
    "teddy_lupin", "lucius_malfoy", "draco", "scorpius",
    "xenophilius_lovegood", "rolf_scamander", "lysander", "lorcan",
    "mr_longbottom", "frank", "neville",
]

mujer = [
    "apolline_delacour", "fleur", "gabrielle", "molly", "audrey",
    "angelina", "hermione", "ginny", "rose", "lily_luna", "molly_ii",
    "lucy", "roxanne", "victoire", "dominique", "lily_evans",
    "petunia_evans", "druella_rosier", "bellatrix", "andromeda",
    "narcissa", "walburga_black", "nymphadora_tonks", "astoria_greengrass",
    "lunas_mum", "luna", "augusta", "alice", "hannah_abbot",
]

casado = [
    ("monsieur_delacour", "apolline_delacour"),
    ("bill", "fleur"),
    ("arthur", "molly"),
    ("percy", "audrey"),
    ("george", "angelina"),
    ("ron", "hermione"),
    ("harry", "ginny"),
    ("james_potter", "lily_evans"),
    ("vernon_dursley", "petunia_evans"),
    ("cygnus_black_iii", "druella_rosier"),
    ("orion_black", "walburga_black"),
    ("bellatrix", "rodolphus_lestrange"),
    ("andromeda", "ted_tonks"),
    ("nymphadora_tonks", "remus_lupin"),
    ("narcissa", "lucius_malfoy"),
    ("draco", "astoria_greengrass"),
    ("xenophilius_lovegood", "lunas_mum"),
    ("luna", "rolf_scamander"),
    ("mr_longbottom", "augusta"),
    ("frank", "alice"),
    ("neville", "hannah_abbot"),
]


def progenitores(x):
    return [p for (p, h) in progenitor if h == x]


def hijos(x):
    return [h for (p, h) in progenitor if p == x]


def esposos(x, y):
    return (x, y) in casado or (y, x) in casado


def hermanos(x):
    return [h for p in progenitores(x) for h in hijos(p) if h != x]


def yerno(ego, persona):
    return persona in hombre and [h for h in hijos(ego) if esposos(h, persona)] != []


def bisnieto_a(ego, persona):
    return persona in [bn for h in hijos(ego) for n in hijos(h) for bn in hijos(n)]


def sobrino_a_nieto(ego, persona):
    return persona in [g for h in hermanos(ego) for x in hijos(h) for g in hijos(x)]


def abuelo_a(ego, persona):
    return persona in [gp for p in progenitores(ego) for gp in progenitores(p)]


def bisabuelos(ego):
    return [ba for p in progenitores(ego) for gp in progenitores(p) for ba in progenitores(gp)]


def tio_bisabuelo_a(ego, persona):
    return persona in [s for ba in bisabuelos(ego) for s in hermanos(ba)]


##R002##
##20##
def descendiente(ego, persona):
    directos = hijos(persona)
    if ego in directos:
        return True
    return [x for x in directos if descendiente(ego, x)] != []


##R003##
##20##
def descendientes(ego):
    directos = hijos(ego)
    return directos + [d for h in directos for d in descendientes(h)]


##R004##
##10##
def seq0(n):
    if n == 0:
        return 7
    return 2 * seq0(n - 1) + 3


##R005##
##35##
grafo = [
    ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"),
    ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "A"),
]


def siguiente(x):
    return [b for (a, b) in grafo if a == x][0]


def imp_graf_cir(inicio, limite):
    print(inicio)
    if inicio == limite:
        return
    imp_graf_cir(siguiente(inicio), limite)


##R006##
##15##
def badaboom(n):
    match (n % 3 == 0, n % 5 == 0):
        case (True, True):
            return "Bada Boom!!"
        case (True, False):
            return "Bada"
        case (False, True):
            return "Boom!!"
        case _:
            return n


##R007##
##15##
def lista_badaboom(n):
    if n == 0:
        return []
    return lista_badaboom(n - 1) + [badaboom(n)]


##R008##
##20##
def pirata(lista, px, py):
    match lista:
        case []:
            return (px, py)
        case ["A", *c]:
            return pirata(c, px, py + 1)
        case ["V", *c]:
            return pirata(c, px, py - 1)
        case [">", *c]:
            return pirata(c, px + 1, py)
        case ["<", *c]:
            return pirata(c, px - 1, py)


##R009##
##10##
def combina_listas(l1, l2):
    match (l1, l2):
        case ([], _):
            return l2
        case (_, []):
            return l1
        case ([x, *xs], [y, *ys]):
            return [x, y] + combina_listas(xs, ys)
