progenitor_a("Arthur Weasley", "Bill Weasley").
progenitor_a("Molly Prewett", "Bill Weasley").
progenitor_a("Arthur Weasley", "Charlie Weasley").
progenitor_a("Molly Prewett", "Charlie Weasley").
progenitor_a("Arthur Weasley", "Percy Weasley").
progenitor_a("Molly Prewett", "Percy Weasley").
progenitor_a("Arthur Weasley", "Fred Weasley").
progenitor_a("Molly Prewett", "Fred Weasley").
progenitor_a("Arthur Weasley", "George Weasley").
progenitor_a("Molly Prewett", "George Weasley").
progenitor_a("Arthur Weasley", "Ron Weasley").
progenitor_a("Molly Prewett", "Ron Weasley").
progenitor_a("Arthur Weasley", "Ginny Weasley").
progenitor_a("Molly Prewett", "Ginny Weasley").
progenitor_a("Bill Weasley", "Victoire Weasley").
progenitor_a("Fleur Delacour", "Victoire Weasley").
progenitor_a("Bill Weasley", "Dominique Weasley").
progenitor_a("Fleur Delacour", "Dominique Weasley").
progenitor_a("Bill Weasley", "Louis Weasley").
progenitor_a("Fleur Delacour", "Louis Weasley").
progenitor_a("Percy Weasley", "Molly Weasley II").
progenitor_a("Audrey", "Molly Weasley II").
progenitor_a("Percy Weasley", "Lucy Weasley").
progenitor_a("Audrey", "Lucy Weasley").
progenitor_a("George Weasley", "Fred Weasley II").
progenitor_a("Angelina Johnson", "Fred Weasley II").
progenitor_a("George Weasley", "Roxanne Weasley").
progenitor_a("Angelina Johnson", "Roxanne Weasley").
progenitor_a("Ron Weasley", "Hugo Weasley").
progenitor_a("Hermione Granger", "Hugo Weasley").
progenitor_a("Ron Weasley", "Rose Weasley").
progenitor_a("Hermione Granger", "Rose Weasley").
progenitor_a("Harry Potter", "James Sirius Potter").
progenitor_a("Ginny Weasley", "James Sirius Potter").
progenitor_a("Harry Potter", "Albus Severus Potter").
progenitor_a("Ginny Weasley", "Albus Severus Potter").
progenitor_a("Harry Potter", "Lily Luna Potter").
progenitor_a("Ginny Weasley", "Lily Luna Potter").
progenitor_a("Septimus Weasley", "Arthur Weasley").
progenitor_a("Cedrella Black", "Arthur Weasley").
progenitor_a("Septimus Weasley", "Balthazar Weasley").
progenitor_a("Cedrella Black", "Balthazar Weasley").
progenitor_a("Balthazar Weasley", "Edmund Weasley").
progenitor_a("Edmund Weasley", "Clara Weasley").
progenitor_a("Hugo Weasley", "Iris Weasley").
pareja_a("Harry Potter", "Ginny Weasley").
pareja_a("Bill Weasley", "Fleur Delacour").
pareja_a("Ron Weasley", "Hermione Granger").

yerno(Ego, Persona) :-
	pareja_a(Ego, Hija),
	progenitor_a(Persona, Hija).

bisnieto_a(Ego, Persona) :-
	bisabuelo_a(Persona, Ego).

sobrino_a_nieto(Ego, Persona) :-
	hermano_a(Hermano, Persona),
	progenitor_a(Hermano, Hijo),
	progenitor_a(Hijo, Ego).

abuelo_a(Ego, Persona) :-
	progenitor_a(Ego, Padre),
	progenitor_a(Padre, Persona).

tio_bisabuelo_a(Ego, Persona) :-
	hermano_a(Ego, Bisabuelo),
	bisabuelo_a(Bisabuelo, Persona).



seq0(0,R) :- R = 7.
seq0(N,R) :-
	N > 0, M is N - 1,
	seq0(M,RM),
	R is 2 * RM + 3.




badaboom(N,R) :-
	Q3 is N mod 3, Q5 is N mod 5,
	Q3 == 0, Q5 == 0,
	R = "Bada Boom!!".
badaboom(N,R) :-
	Q3 is N mod 3, Q5 is N mod 5,
	Q3 == 0, Q5 \== 0,
	R = "Bada".
badaboom(N,R) :-
	Q3 is N mod 3, Q5 is N mod 5,
	Q3 \== 0, Q5 == 0,
	R = "Boom!!".
badaboom(N,R) :-
	Q3 is N mod 3, Q5 is N mod 5,
	Q3 \== 0, Q5 \== 0,
	R = N.


lista_badaboom(N,L) :-
	lista_badaboom_aux(1,N,L).
lista_badaboom_aux(I,N,L) :-
	I > N,
	L = [].
lista_badaboom_aux(I,N,L) :-
	I =< N, badaboom(I,R),
	J is I + 1,
	lista_badaboom_aux(J,N,RR),
	L = [R|RR].

imprimir_listas([],L2,R) :- R = L2.
imprimir_listas([F|C],[],R) :- R = [F|C].
imprimir_listas([F|C],[G|D],R) :-
	imprimir_listas(C,D,RR),
	R = [F,G|RR].

