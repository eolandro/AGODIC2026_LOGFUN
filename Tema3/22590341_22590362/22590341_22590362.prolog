prueba(Titulo, Meta) :-
    format("~w -> ", [Titulo]),
    (   once(Meta)
    ->  writeln(true)
    ;   writeln(false)
    ).
% R001
%  BASE DE CONOCIMIENTOS

% progenitor
progenitor_a("Fleur","Monsieur Delacour").
progenitor_a("Fleur","Apolline").
progenitor_a("Gabrielle","Monsieur Delacour").
progenitor_a("Gabrielle","Apolline").

progenitor_a("Bill","Arthur").
progenitor_a("Bill","Molly").
progenitor_a("Charlie","Arthur").
progenitor_a("Charlie","Molly").
progenitor_a("Percy","Arthur").
progenitor_a("Percy","Molly").
progenitor_a("Fred","Arthur").
progenitor_a("Fred","Molly").
progenitor_a("George","Arthur").
progenitor_a("George","Molly").
progenitor_a("Ronald","Arthur").
progenitor_a("Ronald","Molly").
progenitor_a("Ginevra","Arthur").
progenitor_a("Ginevra","Molly").

progenitor_a("Victoire","Bill").
progenitor_a("Victoire","Fleur").
progenitor_a("Dominique","Bill").
progenitor_a("Dominique","Fleur").
progenitor_a("Louis","Bill").
progenitor_a("Louis","Fleur").

progenitor_a("Molly II","Percy").
progenitor_a("Molly II","Audrey").
progenitor_a("Lucy","Percy").
progenitor_a("Lucy","Audrey").

progenitor_a("Fred II","George").
progenitor_a("Fred II","Esposa de George").
progenitor_a("Roxanne","George").
progenitor_a("Roxanne","Esposa de George").

progenitor_a("Rose","Ronald").
progenitor_a("Rose","Hermione").
progenitor_a("Hugo","Ronald").
progenitor_a("Hugo","Hermione").

progenitor_a("James Sirius","Harry").
progenitor_a("James Sirius","Ginevra").
progenitor_a("Albus Severus","Harry").
progenitor_a("Albus Severus","Ginevra").
progenitor_a("Lily Luna","Harry").
progenitor_a("Lily Luna","Ginevra").

progenitor_a("Harry","James Potter").
progenitor_a("Harry","Lily Evans").
progenitor_a("Dudley","Vernon").
progenitor_a("Dudley","Petunia").

progenitor_a("Bellatrix","Cygnus III").
progenitor_a("Bellatrix","Druella").
progenitor_a("Andromeda","Cygnus III").
progenitor_a("Andromeda","Druella").
progenitor_a("Narcissa","Cygnus III").
progenitor_a("Narcissa","Druella").

progenitor_a("Nymphadora","Ted").
progenitor_a("Nymphadora","Andromeda").
progenitor_a("Teddy","Remus").
progenitor_a("Teddy","Nymphadora").
progenitor_a("Draco","Lucius").
progenitor_a("Draco","Narcissa").
progenitor_a("Scorpius","Draco").
progenitor_a("Scorpius","Astoria").

progenitor_a("Sirius","Orion").
progenitor_a("Sirius","Walburga").
progenitor_a("Regulus","Orion").
progenitor_a("Regulus","Walburga").

progenitor_a("Frank","Mr Longbottom").
progenitor_a("Frank","Augusta").
progenitor_a("Neville","Frank").
progenitor_a("Neville","Alice").

progenitor_a("Luna","Xenophilius").
progenitor_a("Luna","Madre de Luna").
progenitor_a("Lorcan","Rolf").
progenitor_a("Lorcan","Luna").
progenitor_a("Lysander","Rolf").
progenitor_a("Lysander","Luna").

% parejas
pareja("Rodolphus","Bellatrix").
pareja("Neville","Hannah").
pareja("Victoire","Teddy").
pareja("Rose","Scorpius").

% hermanos sin padre en el arbol
hermano_a("Marjorie","Vernon").
hermano_a("Cygnus III","Walburga").
hermano_a("Astoria","Daphne").
hermano_a("Lily Evans","Petunia").

% genero
hombre("Monsieur Delacour").
hombre("Arthur").
hombre("Bill").
hombre("Charlie").
hombre("Percy").
hombre("Fred").
hombre("George").
hombre("Ronald").
hombre("Louis").
hombre("Fred II").
hombre("Hugo").
hombre("Harry").
hombre("James Sirius").
hombre("Albus Severus").
hombre("James Potter").
hombre("Vernon").
hombre("Dudley").
hombre("Cygnus III").
hombre("Ted").
hombre("Remus").
hombre("Teddy").
hombre("Lucius").
hombre("Draco").
hombre("Scorpius").
hombre("Orion").
hombre("Sirius").
hombre("Regulus").
hombre("Mr Longbottom").
hombre("Frank").
hombre("Neville").
hombre("Xenophilius").
hombre("Rolf").
hombre("Lorcan").
hombre("Lysander").
hombre("Rodolphus").

mujer("Apolline").
mujer("Fleur").
mujer("Gabrielle").
mujer("Molly").
mujer("Ginevra").
mujer("Victoire").
mujer("Dominique").
mujer("Audrey").
mujer("Molly II").
mujer("Lucy").
mujer("Esposa de George").
mujer("Roxanne").
mujer("Hermione").
mujer("Rose").
mujer("Lily Luna").
mujer("Lily Evans").
mujer("Petunia").
mujer("Marjorie").
mujer("Druella").
mujer("Bellatrix").
mujer("Andromeda").
mujer("Narcissa").
mujer("Nymphadora").
mujer("Astoria").
mujer("Daphne").
mujer("Walburga").
mujer("Augusta").
mujer("Alice").
mujer("Hannah").
mujer("Madre de Luna").
mujer("Luna").

%  REGLAS AUXILIARES

% Hermanos
hermanos(X,Y) :- hermano_a(X,Y).
hermanos(X,Y) :- hermano_a(Y,X).
hermanos(X,Y) :- X \== Y, progenitor_a(X,P), progenitor_a(Y,P).

% Conyuge
conyuge(X,Y) :- pareja(X,Y).
conyuge(X,Y) :- pareja(Y,X).
conyuge(X,Y) :- X \== Y, progenitor_a(H,X), progenitor_a(H,Y).

% Persona es abuelo/a de Ego
abuelo_a(Ego,Persona) :-
    progenitor_a(Ego,PaMa),
    progenitor_a(PaMa,Persona).

% Ego es abuelo/a de Persona
nieto_a(Ego,Persona) :-
    abuelo_a(Persona,Ego).

% Persona es bisabuelo/a de Ego
bisabuelo_a(Ego,Persona) :-
    progenitor_a(Ego,PaMa),
    abuelo_a(PaMa,Persona).

%  PREDICADOS

% Persona es yerno de Ego
yerno(Ego,Persona) :-
    progenitor_a(Hija,Ego),
    mujer(Hija),
    conyuge(Hija,Persona),
    hombre(Persona).

% Persona es bisnieto/a de Ego
bisnieto_a(Ego,Persona) :-
    bisabuelo_a(Persona,Ego).

% Persona es sobrino/a nieto/a de Ego
sobrino_a_nieto(Ego,Persona) :-
    hermanos(Ego,Hermano),
    nieto_a(Hermano,Persona).

% abuelo_a(Ego,Persona): definido arriba

% Persona es tio/a bisabuelo/a de Ego
tio_bisabuelo_a(Ego,Persona) :-
    bisabuelo_a(Ego,Bisabuelo),
    hermanos(Bisabuelo,Persona).

% consultas probadas
% yerno("Arthur","Harry").                 % true
% yerno("Arthur","Hermione").              % false
% bisnieto_a("Cygnus III","Scorpius").     % true
% abuelo_a("Draco","Cygnus III").          % true
% sobrino_a_nieto("Walburga","Draco").     % true
% tio_bisabuelo_a("Scorpius","Walburga").  % true
% tio_bisabuelo_a("Scorpius","Orion").     % false

:- writeln("R001: Consultas probadas").
:- prueba("yerno(Arthur,Harry)", yerno("Arthur","Harry")).
:- prueba("yerno(Arthur,Hermione)", yerno("Arthur","Hermione")).
:- prueba("bisnieto_a(Cygnus III,Scorpius)", bisnieto_a("Cygnus III","Scorpius")).
:- prueba("sobrino_a_nieto(Walburga,Draco)", sobrino_a_nieto("Walburga","Draco")).
:- prueba("abuelo_a(Draco,Cygnus III)", abuelo_a("Draco","Cygnus III")).
:- prueba("tio_bisabuelo_a(Scorpius,Walburga)", tio_bisabuelo_a("Scorpius","Walburga")).
:- prueba("tio_bisabuelo_a(Scorpius,Orion)", tio_bisabuelo_a("Scorpius","Orion")).

%R004
% 7, 17, 37, 77, 157, 317  ->  a(0)=7, a(n)=2*a(n-1)+3
seq0(0, 7).
seq0(N, R) :-
    N > 0,
    N1 is N - 1,
    seq0(N1, R1),
    R is R1 * 2 + 3.

:- writeln("R004").
:- forall(member(N, [0,1,2,3,4,5]),
          ( seq0(N, R), format("seq0(~w) = ~w~n", [N, R]) )).

%R005
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
:- writeln("R005").
:- writeln("imp_graf_cir(A,E):"), once(imp_graf_cir("A","E")).
:- writeln("imp_graf_cir(A,G):"), once(imp_graf_cir("A","G")).

%R006
badaboom(N, "Bada Boom!!") :-
    0 is N mod 3,
    0 is N mod 5.
badaboom(N, "Bada") :-
    0 is N mod 3,
    N mod 5 =\= 0.
badaboom(N, "Boom!!") :-
    0 is N mod 5,
    N mod 3 =\= 0.
badaboom(N, N) :-
    N mod 3 =\= 0,
    N mod 5 =\= 0.
:- writeln("R006").
:- forall(member(N, [15,10,6,7]),
          ( once(badaboom(N, R)), format("badaboom(~w) = ~w~n", [N, R]) )).

%R007
lista_badaboom(N, L) :-
    generar_lista(1, N, L).

generar_lista(Actual, N, []) :-
    Actual > N.
generar_lista(Actual, N, [P|R]) :-
    Actual =< N,
    badaboom(Actual, P),
    Siguiente is Actual + 1,
    generar_lista(Siguiente, N, R).
:- writeln("R007").
:- lista_badaboom(20, L), format("lista_badaboom(20) = ~w~n", [L]).

%R008
pirata([], X, Y, X, Y).
pirata(["A"|C], PX, PY, RX, RY) :-
    PY1 is PY + 1,
    pirata(C, PX, PY1, RX, RY).
pirata(["V"|C], PX, PY, RX, RY) :-
    PY1 is PY - 1,
    pirata(C, PX, PY1, RX, RY).
pirata([">"|C], PX, PY, RX, RY) :-
    PX1 is PX + 1,
    pirata(C, PX1, PY, RX, RY).
pirata(["<"|C], PX, PY, RX, RY) :-
    PX1 is PX - 1,
    pirata(C, PX1, PY, RX, RY).
:- writeln("R008").
:- pirata(["A","A","A","<","V","V"], 0, 0, X, Y),
   format("pirata desde (0,0) = (~w,~w)~n", [X, Y]).
:- pirata(["A","A","A","<","V","V"], 5, 5, X, Y),
   format("pirata desde (5,5) = (~w,~w)~n", [X, Y]).
:- pirata(["A","A","A","<","V","V"], 0, -2, X, Y),
   format("pirata desde (0,-2) = (~w,~w)~n", [X, Y]).

%R009
combina_listas([], L2, L2).
combina_listas([F|C], [], [F|C]).
combina_listas([F|C], [G|D], [F,G|R]) :-
    combina_listas(C, D, R).

:- writeln("R009").
:- combina_listas([1,2,3], ["a","b","c"], R), format("~w~n", [R]).
:- combina_listas([1], ["a","b","c"], R), format("~w~n", [R]).
:- combina_listas([1,2,3], ["a"], R), format("~w~n", [R]).