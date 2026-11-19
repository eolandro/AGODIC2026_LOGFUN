% Oliver Uriel Pagola Perez 23590114
% Javier Yael Enriquez Martinez 22590324

% ##R004##
% ##10##
seq0(0, R) :-
    R = 7.
seq0(N, R) :-
    number(N),
    N > 0,
    N1 is N - 1,
    seq0(N1, R1),
    R is 2 * R1 + 3.

%--------------------------------------------------------------
% ##R005##
% ##35##
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

imp_graf_cir(Inicio, Limite) :-
    Inicio == Limite,
    writeln(Inicio).

imp_graf_cir(Inicio, Limite) :-
    Inicio \== Limite,
    writeln(Inicio),
    grafo(Inicio, Siguiente),
    imp_graf_cir(Siguiente, Limite).

%--------------------------------------------------------------
% ##R006##
% ##15##
badaboom(N, R) :-
    number(N),
    M3 is N mod 3,
    M5 is N mod 5,
    M3 == 0,
    M5 == 0,
    R = "Bada Boom!!".

badaboom(N, R) :-
    number(N),
    M3 is N mod 3,
    M5 is N mod 5,
    M3 == 0,
    M5 =\= 0,
    R = "Bada".

badaboom(N, R) :-
    number(N),
    M3 is N mod 3,
    M5 is N mod 5,
    M3 =\= 0,
    M5 == 0,
    R = "Boom!!".

badaboom(N, R) :-
    number(N),
    M3 is N mod 3,
    M5 is N mod 5,
    M3 =\= 0,
    M5 =\= 0,
    R = N.

%--------------------------------------------------------------
% ##R007##
% ##15##
lista_badaboom_aux(Actual, Limite, L) :-
    Actual == Limite,
    badaboom(Actual, Elem),
    L = [Elem].

lista_badaboom_aux(Actual, Limite, L) :-
    Actual < Limite,
    badaboom(Actual, Elem),
    Siguiente is Actual + 1,
    lista_badaboom_aux(Siguiente, Limite, Resto),
    L = [Elem | Resto].

lista_badaboom(N, L) :-
    number(N),
    N >= 1,
    lista_badaboom_aux(1, N, L).

%--------------------------------------------------------------
% ##R008##
% ##20##
pirata([], PX, PY, RX, RY) :-
    RX = PX,
    RY = PY.

pirata(["A" | C], PX, PY, RX, RY) :-
    NY is PY + 1,
    pirata(C, PX, NY, RX, RY).

pirata(["V" | C], PX, PY, RX, RY) :-
    NY is PY - 1,
    pirata(C, PX, NY, RX, RY).

pirata([">" | C], PX, PY, RX, RY) :-
    NX is PX + 1,
    pirata(C, NX, PY, RX, RY).

pirata(["<" | C], PX, PY, RX, RY) :-
    NX is PX - 1,
    pirata(C, NX, PY, RX, RY).

%--------------------------------------------------------------
% ##R009##
% ##10##
combina_listas([], L2, R) :-
    R = L2.
combina_listas([F | C], [], R) :-
    R = [F | C].
combina_listas([F | C], [G | D], R) :-
    combina_listas(C, D, RC),
    R = [F, G | RC].
