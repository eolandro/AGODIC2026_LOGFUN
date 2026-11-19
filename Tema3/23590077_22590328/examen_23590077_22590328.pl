/*ejercicio 1
-------------------------------------------------------

*/

/*ejercicio 2
-------------------------------------------------------

*/

/*ejercicio 3
-------------------------------------------------------

*/



/*ejercicio 4
-------------------------------------------------------
##R004##
##10##

"""

Dada la siguiente secuencia matematica
7, 17, 37, 77, 157, 317
Encuentre la función matematica recursiva
e implementela en prolog

seq0(N,R).
	
seq0(0,R).
#R = 7
seq0(1,R).
#R = 17
seq0(2,R).
#R = 37

"""
[a(0) = 7]
[a(N) = 2 * a(N-1) + 3]

*/
seq0(0,7).
seq0(N,R) :-
    N > 0,
    N1 is N - 1,
    seq0(N1,R1),
    R is 2 * R1 + 3.

/*ejercicio 5
-------------------------------------------------------
##R005##
##35##
"""

Recorrido en un grafo circular
Defina una funcion recursiva que imprima todos
los elementos de un grafo circular

A → B → C → D → E
↑               ↓
J → I → H → G → F


grafo("A","B").
grafo("B","C").
grafo("C","D").
grafo("D","E").
grafo("E","F").
grafo("F","G").
grafo("G","H").
grafo("H","I").
grafo("I","J").
grafo("J","A").



imp_graf_cir(Inicio,Limite).

imp_graf_cir("A","E").
#A
#B
#C
#D
#E
imp_graf_cir("A","G").
#A
#B
#C
#D
#E
#F
#G
imp_graf_cir("A","J").
#A
#B
#C
#D
#E
#F
#G
#H
#I
#J
"""
*/
grafo("A","B").
grafo("B","C").
grafo("C","D").
grafo("D","E").
grafo("E","F").
grafo("F","G").
grafo("G","H").
grafo("H","I").
grafo("I","J").
grafo("J","A").

imp_graf_cir(Limite, Limite) :-
    writeln(Limite).
imp_graf_cir(Inicio, Limite) :-
    Inicio \== Limite,
    writeln(Inicio),
    grafo(Inicio, Siguiente),
    imp_graf_cir(Siguiente, Limite).




/*ejercicio 6
-------------------------------------------------------
"""
##R006##
##15##
"""
Bada Boom!!! Parte 1
define un predicado que dado un numero entero te devuelva un 
resultado segun las siguientes condiciones:
	1) Si es multiplo de 3 coloque la cadena "Bada"
	2) Si es multiplo de 5 coloque la cadena "Boom!!"
	3) Si es multiplo de 3 y 5 coloque "Bada Boom!!"
	4) El mismo numero si no cae en los casos anteriores
	
badaboom(N,R)
	
badaboom(15,R).
R = "Bada Boom!!"

badaboom(10,R).
R = "Boom!!"

badaboom(6,R).
R = "Bada"


"""
*/
badaboom(N,"Bada Boom!!") :-
    N mod 3 =:= 0,
    N mod 5 =:= 0.
badaboom(N, "Bada") :-
    N mod 3 =:= 0,
    N mod 5 =\= 0.
badaboom(N, "Boom!!") :-
    N mod 3 =\= 0,
    N mod 5 =:= 0.
badaboom(N, N) :-
    N mod 3 =\= 0,
    N mod 5 =\= 0.





/*ejercicio 7
-------------------------------------------------------

##R007##
##15##
"""
Bada Boom!!! Parte 2

Define un predicado retorne una lista con los numeros del 1 hasta N
aplicando el predicado Badaboom
	
N = 100
lista_badaboom(100,L)
L = [1,2,"Bada",4,"Boom!!","Bada",7,8,"Bada","Boom!!",11,"Bada",13,14,"BadaBoom!!"...

"""
*/

lista_badaboom(0, []).
lista_badaboom(N, L) :-
    N > 0,\
    N1 is N - 1,
    lista_badaboom(N1, L1),
    badaboom(N, R),
    append(L1, [R], L).

/*ejercicio 8
-------------------------------------------------------
##R008##
##20##
"""
Mapa del tesoro

Un pirata ha escondido un tesoro en una isla
para saber su ubicacion ha realizado un mapa que
describe cuantos pasos debe caminar desde un punto 
conocido para encontrarlo.

para realizar lo anterior ha definido unos simbolos
que le ayudan a determinar la posicion y la cantidad de
pasos

A =  arriba
V =  abajo
> =  derecha
< =  izquierda

Ejemplo:

2 Pasos a la derecha y 3 abajo

equivale a

>>VVV


3 arriba, 1 izquierda y 2 abajo

AAA<VV

Realiza un predicado en prolog que resuelva donde esta el tesoro
dada una lista de simbolos y un punto PX,PY inicial considerando que:

arriba ==> incrementa Y
abajo  ==> decrementa Y
derecha ==> incrementa X
izquierda ==> decrementa X

pirata([F|C],PX,PY,RX,RY). 
pirata(["A","A","A","<","V","V"],0,0,RX,RY).
RX = -1.
RY = 1.
true.

pirata(["A","A","A","<","V","V"],5,5,RX,RY).
RX = 4.
RY = 6.
true.

pirata(["A","A","A","<","V","V"],0,-2,RX,RY).
RX = -1.
RY = -1.
true.
"""
*/


pirata([], PX, PY, PX, PY).
pirata(["A"|C], PX, PY, RX, RY) :-
    NY is PY + 1,
    pirata(C, PX, NY, RX, RY).

pirata(["V"|C], PX, PY, RX, RY) :-
    NY is PY - 1,
    pirata(C, PX, NY, RX, RY).

pirata([">"|C], PX, PY, RX, RY) :-
    NX is PX + 1,
    pirata(C, NX, PY, RX, RY).

pirata(["<"|C], PX, PY, RX, RY) :-
    NX is PX - 1,
    pirata(C, NX, PY, RX, RY).



/*ejercicio 9
-------------------------------------------------------

##R009##
##10##
"""
Combinar Listas 

Una funcion toma dos listas L1 y L2, las une en una sola
combiando primer elemento de L1 con el primer elemento de L2.

Si una de las dos listas se agota simplemente une el resto de la lista a
la lista resultante


combina_listas([F|C],[G|D],R).

combina_listas([1,2,3],["a","b","c"],R).
R =  [1,"a",2,"b",3,"c"].


combina_listas([1],["a","b","c"],R).
R = [1,"a","b","c"]

combina_listas([1,2,3],["a"],R).
R = [1,"a",2,3]

*/
combina_listas([], L2, L2).
combina_listas(L1, [], L1).
combina_listas([P|S], [P2|S2], [P,P2 |R]) :-
    combina_listas(S, S2, R).