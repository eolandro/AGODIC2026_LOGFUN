/*
 Examen 3
 Guillermo Daniel Lopez Garcia
 Leonardo Emmanuel Buendia Ramos
*/


progenitor_a("Harry James Potter","James Potter").
progenitor_a("Harry James Potter","Lily Evans").

progenitor_a("James Sirius Potter","Harry James Potter").
progenitor_a("James Sirius Potter","Ginevra Molly Weasley").
progenitor_a("Albus Severus Potter","Harry James Potter").
progenitor_a("Albus Severus Potter","Ginevra Molly Weasley").
progenitor_a("Lily Luna Potter","Harry James Potter").
progenitor_a("Lily Luna Potter","Ginevra Molly Weasley").


progenitor_a("Dudley Dursley","Vernon Dursley").
progenitor_a("Dudley Dursley","Petunia Evans").


progenitor_a("Bill Arthur Weasley","Arthur Weasley").
progenitor_a("Bill Arthur Weasley","Molly Prewett").
progenitor_a("Charlie Weasley","Arthur Weasley").
progenitor_a("Charlie Weasley","Molly Prewett").
progenitor_a("Fred Weasley","Arthur Weasley").
progenitor_a("Fred Weasley","Molly Prewett").
progenitor_a("Percy Ignatius Weasley","Arthur Weasley").
progenitor_a("Percy Ignatius Weasley","Molly Prewett").
progenitor_a("George Weasley","Arthur Weasley").
progenitor_a("George Weasley","Molly Prewett").
progenitor_a("Ronald Bilius Weasley","Arthur Weasley").
progenitor_a("Ronald Bilius Weasley","Molly Prewett").
progenitor_a("Ginevra Molly Weasley","Arthur Weasley").
progenitor_a("Ginevra Molly Weasley","Molly Prewett").

progenitor_a("Fleur Isabelle Delacour","Monsieur Delacour").
progenitor_a("Fleur Isabelle Delacour","Apolline Delacour").

progenitor_a("Victoire Weasley","Bill Arthur Weasley").
progenitor_a("Victoire Weasley","Fleur Isabelle Delacour").
progenitor_a("Dominique Weasley","Bill Arthur Weasley").
progenitor_a("Dominique Weasley","Fleur Isabelle Delacour").
progenitor_a("Louis Weasley","Bill Arthur Weasley").
progenitor_a("Louis Weasley","Fleur Isabelle Delacour").

progenitor_a("Molly Weasley II","Percy Ignatius Weasley").
progenitor_a("Molly Weasley II","Audrey").
progenitor_a("Lucy Weasley","Percy Ignatius Weasley").
progenitor_a("Lucy Weasley","Audrey").

progenitor_a("Fred Weasley II","George Weasley").
progenitor_a("Fred Weasley II","Angelina Johnson").
progenitor_a("Roxanne Weasley","George Weasley").
progenitor_a("Roxanne Weasley","Angelina Johnson").

progenitor_a("Hugo Weasley","Ronald Bilius Weasley").
progenitor_a("Hugo Weasley","Hermione Jean Granger").
progenitor_a("Rose Weasley","Ronald Bilius Weasley").
progenitor_a("Rose Weasley","Hermione Jean Granger").


progenitor_a("Bellatrix Black","Cygnus Black III").
progenitor_a("Bellatrix Black","Druella Rosier").
progenitor_a("Andromeda Black","Cygnus Black III").
progenitor_a("Andromeda Black","Druella Rosier").
progenitor_a("Narcissa Black","Cygnus Black III").
progenitor_a("Narcissa Black","Druella Rosier").

progenitor_a("Nymphadora Tonks","Andromeda Black").
progenitor_a("Nymphadora Tonks","Ted Tonks").

progenitor_a("Teddy Remus Lupin","Nymphadora Tonks").
progenitor_a("Teddy Remus Lupin","Remus Lupin").

progenitor_a("Draco Lucius Malfoy","Lucius Malfoy").
progenitor_a("Draco Lucius Malfoy","Narcissa Black").

progenitor_a("Scorpius Hyperion Malfoy","Draco Lucius Malfoy").
progenitor_a("Scorpius Hyperion Malfoy","Astoria Greengrass").

progenitor_a("Cygnus Black III","Pollux Black").
progenitor_a("Cygnus Black III","Irma Crabbe").
progenitor_a("Walburga Black","Pollux Black").
progenitor_a("Walburga Black","Irma Crabbe").

progenitor_a("Sirius Black","Orion Black").
progenitor_a("Sirius Black","Walburga Black").
progenitor_a("Regulus Arcturus Black","Orion Black").
progenitor_a("Regulus Arcturus Black","Walburga Black").

/*
 ##R001##
*/

abuelo_a(Ego, Respuesta) :- 
    progenitor_a(Ego,PaMa), 
    progenitor_a(PaMa,Respuesta).


bisabuelo_a(Ego, Persona) :-
    Ego \== Persona,
    abuelo_a(Ego, BA),
    progenitor_a(BA, Persona).

% bisabuelo_a("Scorpius Hyperion Malfoy", "Cygnus Black III").


bisnieto_a(Ego, Persona) :-
    Ego \== Persona,
    bisabuelo_a(Persona, Ego).

% bisnieto_a("Cygnus Black III","Scorpius Hyperion Malfoy").


sobrino_a_nieto(Ego,Persona) :-
    progenitor_a(Ego,PaMa),
    progenitor_a(Hermano_a, PaMa),
    Ego \== Hermano_a,
    progenitor_a(Hijo, Hermano_a),
    progenitor_a(Persona, Hijo).

% sobrino_a_nieto("Bellatrix Black","Teddy Remus Lupin").


yerno_a(Ego,Persona) :-
    progenitor_a(Hijo, Ego),
    progenitor_a(Nieto, Hijo),
    progenitor_a(Nieto, Persona),
    Ego \== Persona,
    Hijo \== Persona.

% yerno_a("Arthur Weasley", "Harry James Potter").


hermano_a(Ego, Persona) :-
    Ego \== Persona, progenitor_a(Ego,PaMa), 
    progenitor_a(Persona,PaMa).

tio_bisabuelo_a(Ego, Persona) :-
    bisabuelo_a(Ego, BA),
    hermano_a(BA, Persona).

% tio_bisabuelo_a("Teddy Remus Lupin", "Walburga Black").


/*
 ##R002##
*/

% Por si el descendiente es directo
descendiente(EGO,PERSONA2) :-
    EGO \== PERSONA2,
    progenitor_a(EGO,PERSONA2).

% descendiente("Lily Luna Potter","Harry James Potter").

% Si no es directo, se vuelve a llamar

descendiente(EGO,PERSONA2) :-
    EGO \== PERSONA2,
    progenitor_a(EGO,PaMa),
    descendiente(PaMa,PERSONA2).

% descendiente("Lily Luna Potter","Molly Prewett").

/*
 ##R003##
*/

descendientes(EGO, ListaDESCENDIENTES) :-
    findall(X, descendiente(X, EGO), ListaDESCENDIENTES).


% descendientes("James Potter",X).


/*
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
*/

seq0(0,R) :-
	R = 7.
seq0(N,R) :-
	N > 0,
	N1 is N - 1,
	seq0(N1,RA),
	R is RA * 2 + 3.

/*
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

imp_graf_cir(Inicio,Limite) :-
	Inicio == Limite,
	writeln(Inicio).
imp_graf_cir(Inicio,Limite) :-
	Inicio \== Limite,
	writeln(Inicio),
	grafo(Inicio,Siguiente),
	imp_graf_cir(Siguiente,Limite).



/*
##R006##
##15##
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
*/

badaboom(N,R) :-
	Q3 is N mod 3,
	Q5 is N mod 5,
	Q3 == 0,
	Q5 == 0,
	R = "Bada Boom!!".
badaboom(N,R) :-
	Q3 is N mod 3,
	Q5 is N mod 5,
	Q3 == 0,
	Q5 \== 0,
	R = "Bada".
badaboom(N,R) :-
	Q3 is N mod 3,
	Q5 is N mod 5,
	Q3 \== 0,
	Q5 == 0,
	R = "Boom!!".
badaboom(N,R) :-
	Q3 is N mod 3,
	Q5 is N mod 5,
	Q3 \== 0,
	Q5 \== 0,
	R = N.


/*
##R007##
##15##
Bada Boom!!! Parte 2

Define un predicado retorne una lista con los numeros del 1 hasta N
aplicando el predicado Badaboom
	
/* N = 100 */
lista_badaboom(100,L)
L = [1,2,"Bada",4,"Boom!!","Bada",7,8,"Bada","Boom!!",11,"Bada",13,14,"BadaBoom!!"...
*/

lista_badaboom(1,L) :-
	badaboom(1,R),
	L = [R].
lista_badaboom(N,L) :-
	N >= 2,
	N1 is N - 1,
	lista_badaboom(N1,LR),
	badaboom(N,R),
	append(LR,[R],L).


/*
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
"""
*/

combina_listas([],L2,R) :-
	R = L2.
combina_listas([F|C],[],R) :-
	R = [F|C].
combina_listas([F|C],[G|D],R) :-
	combina_listas(C,D,RR),
	append([F,G],RR,R).

