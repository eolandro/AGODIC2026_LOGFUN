%%R001%%
%%50%%
/*
Arbol genealogico de Harry Potter (version ampliada)
Hechos base: padre(Padre, Hijo)
*/

% Familia Weasley
padre(arthur_weasley,    bill_weasley).
padre(molly_prewett,     bill_weasley).
padre(arthur_weasley,    charlie_weasley).
padre(molly_prewett,     charlie_weasley).
padre(arthur_weasley,    percy_weasley).
padre(molly_prewett,     percy_weasley).
padre(arthur_weasley,    fred_weasley).
padre(molly_prewett,     fred_weasley).
padre(arthur_weasley,    george_weasley).
padre(molly_prewett,     george_weasley).
padre(arthur_weasley,    ron_weasley).
padre(molly_prewett,     ron_weasley).
padre(arthur_weasley,    ginny_weasley).
padre(molly_prewett,     ginny_weasley).

% Familia Delacour
padre(monsieur_delacour, fleur_delacour).
padre(apolline_delacour, fleur_delacour).
padre(monsieur_delacour, gabrielle_delacour).
padre(apolline_delacour, gabrielle_delacour).

% Bill + Fleur
padre(bill_weasley,      victoire_weasley).
padre(fleur_delacour,    victoire_weasley).
padre(bill_weasley,      dominique_weasley).
padre(fleur_delacour,    dominique_weasley).
padre(bill_weasley,      louis_weasley).
padre(fleur_delacour,    louis_weasley).

% Percy + Audrey
padre(percy_weasley,     molly_weasley_ii).
padre(audrey,            molly_weasley_ii).
padre(percy_weasley,     lucy_weasley).
padre(audrey,            lucy_weasley).

% George + Angelina (implicita, usamos audrey2 para no chocar nombres)
padre(george_weasley,    fred_weasley_ii).
padre(angelina,          fred_weasley_ii).
padre(george_weasley,    roxanne_weasley).
padre(angelina,          roxanne_weasley).

% Ron + Hermione
padre(ron_weasley,       hugo_weasley).
padre(hermione_granger,  hugo_weasley).
padre(ron_weasley,       rose_weasley).
padre(hermione_granger,  rose_weasley).

% Harry + Ginny
padre(harry_potter,      james_sirius_potter).
padre(ginny_weasley,     james_sirius_potter).
padre(harry_potter,      albus_severus_potter).
padre(ginny_weasley,     albus_severus_potter).
padre(harry_potter,      lily_luna_potter).
padre(ginny_weasley,     lily_luna_potter).

% Familia Potter/Evans
padre(james_potter,      harry_potter).
padre(lily_evans,        harry_potter).

% bisabuelos de Lily y Petunia (no estan en la imagen, se infiere que son hermanas)
padre(abuelo_evans,      lily_evans).
padre(abuela_evans,      lily_evans).
padre(abuelo_evans,      petunia_evans).
padre(abuela_evans,      petunia_evans).

% Vernon + Petunia
padre(vernon_dursley,    dudley_dursley).
padre(petunia_evans,     dudley_dursley).

% Familia Black / Malfoy
padre(cygnus_black_iii,  bellatrix_black).
padre(druella_rosier,    bellatrix_black).
padre(cygnus_black_iii,  andromeda_black).
padre(druella_rosier,    andromeda_black).
padre(cygnus_black_iii,  narcissa_black).
padre(druella_rosier,    narcissa_black).

padre(lucius_malfoy,     draco_malfoy).
padre(narcissa_black,    draco_malfoy).

padre(draco_malfoy,      scorpius_malfoy).
padre(astoria_greengrass, scorpius_malfoy).

% Andromeda + Ted Tonks
padre(ted_tonks,         nymphadora_tonks).
padre(andromeda_black,   nymphadora_tonks).

% Remus + Nymphadora
padre(remus_lupin,       teddy_lupin).
padre(nymphadora_tonks,  teddy_lupin).

% Familia Longbottom
padre(frank_longbottom,  neville_longbottom).
padre(alice,             neville_longbottom).

% Familia Lovegood
padre(xenophilius_lovegood, luna_lovegood).
padre(lunas_mum,             luna_lovegood).

% Luna + Rolf
padre(rolf_scamander,    lorcan_scamander).
padre(luna_lovegood,     lorcan_scamander).
padre(rolf_scamander,    lysander_scamander).
padre(luna_lovegood,     lysander_scamander).

% Orion + Walburga Black
padre(orion_black,       sirius_black).
padre(walburga_black,    sirius_black).
padre(orion_black,       regulus_black).
padre(walburga_black,    regulus_black).

% Bisabuelo comun de Orion y Cygnus (para tio_bisabuelo_a)
padre(arcturus_black,    orion_black).
padre(arcturus_black,    cygnus_black_iii).

% Genero
hombre(arthur_weasley). hombre(bill_weasley). hombre(charlie_weasley).
hombre(percy_weasley).  hombre(fred_weasley). hombre(george_weasley).
hombre(ron_weasley).    hombre(hugo_weasley). hombre(louis_weasley).
hombre(james_potter).   hombre(harry_potter). hombre(dudley_dursley).
hombre(vernon_dursley). hombre(lucius_malfoy). hombre(draco_malfoy).
hombre(scorpius_malfoy). hombre(ted_tonks).   hombre(remus_lupin).
hombre(teddy_lupin).    hombre(neville_longbottom). hombre(frank_longbottom).
hombre(xenophilius_lovegood). hombre(rolf_scamander). hombre(lorcan_scamander).
hombre(lysander_scamander).   hombre(sirius_black).   hombre(regulus_black).
hombre(orion_black).    hombre(monsieur_delacour).    hombre(fred_weasley_ii).
hombre(james_sirius_potter). hombre(albus_severus_potter). hombre(cygnus_black_iii).
hombre(arcturus_black). hombre(abuelo_evans).

mujer(molly_prewett).    mujer(apolline_delacour). mujer(fleur_delacour).
mujer(gabrielle_delacour). mujer(ginny_weasley).   mujer(hermione_granger).
mujer(lily_evans).       mujer(petunia_evans).     mujer(narcissa_black).
mujer(bellatrix_black).  mujer(andromeda_black).   mujer(druella_rosier).
mujer(nymphadora_tonks). mujer(alice).             mujer(lunas_mum).
mujer(luna_lovegood).    mujer(walburga_black).     mujer(audrey).
mujer(rose_weasley).     mujer(victoire_weasley).  mujer(dominique_weasley).
mujer(roxanne_weasley).  mujer(molly_weasley_ii).  mujer(lucy_weasley).
mujer(lily_luna_potter). mujer(astoria_greengrass). mujer(hannah_abbot).
mujer(daphne_greengrass). mujer(angelina).          mujer(abuela_evans).

casado(bill_weasley,     fleur_delacour).
casado(arthur_weasley,   molly_prewett).
casado(ron_weasley,      hermione_granger).
casado(harry_potter,     ginny_weasley).
casado(george_weasley,   angelina).
casado(percy_weasley,    audrey).
casado(remus_lupin,      nymphadora_tonks).
casado(draco_malfoy,     astoria_greengrass).
casado(ted_tonks,        andromeda_black).
casado(lucius_malfoy,    narcissa_black).
casado(neville_longbottom, hannah_abbot).
casado(rolf_scamander,   luna_lovegood).
casado(james_potter,     lily_evans).
casado(vernon_dursley,   petunia_evans).
casado(frank_longbottom, alice).
casado(orion_black,      walburga_black).
casado(cygnus_black_iii, druella_rosier).

% yerno(Ego, Persona): esposo de la hija de Ego
yerno(Ego, Persona) :-
    padre(Ego, Hija), mujer(Hija),
    casado(Persona, Hija), hombre(Persona).

% bisnieto_a(Ego, Persona): 3 generaciones abajo
bisnieto_a(Ego, Persona) :-
    padre(Ego, H1), padre(H1, H2), padre(H2, Persona).

% sobrino_a_nieto(Ego, Persona): Ego es sobrino-nieto de Persona
% (hijo del sobrino de Persona) -> equivalente a sobrino_nieto(Persona, Ego)
sobrino_a_nieto(Ego, Persona) :-
    padre(Ab, Persona), padre(Ab, Herm), Herm \= Persona,
    padre(Herm, Sob), padre(Sob, Ego).

% abuelo_a(Ego, Persona): 2 generaciones abajo
abuelo_a(Ego, Persona) :-
    padre(Ego, P), padre(P, Persona).

% tio_bisabuelo_a(Ego, Persona): hermano del bisabuelo de Persona
tio_bisabuelo_a(Ego, Persona) :-
    padre(Tatarabuelo, Ego),
    padre(Tatarabuelo, Bisabuelo), Bisabuelo \= Ego,
    padre(Bisabuelo, Abuelo),
    padre(Abuelo, Padre),
    padre(Padre, Persona).

%%R002%%
%%20%%
descendiente(Ego, Persona) :- padre(Persona, Ego).
descendiente(Ego, Persona) :- padre(Persona, I), descendiente(Ego, I).

%%R003%%
%%20%%
descendientes(Ego, L) :- findall(D, descendiente(D, Ego), L).

%%R004%%
%%10%%
seq0(0, 7).
seq0(N, R) :- N > 0, N1 is N-1, seq0(N1, R1), R is 2*R1 + 3.

%%R005%%
%%35%%
grafo("A","B"). grafo("B","C"). grafo("C","D"). grafo("D","E").
grafo("E","F"). grafo("F","G"). grafo("G","H"). grafo("H","I").
grafo("I","J"). grafo("J","A").

imp_graf_cir(L, L)  :- writeln(L).
imp_graf_cir(A, L)  :- A\=L, writeln(A), grafo(A,S), imp_graf_cir(S,L).

%%R006%%
%%15%%
/*
Bada Boom!! Parte 1
*/
badaboom(N, "Bada Boom!!") :- 0 is N mod 3, 0 is N mod 5.
badaboom(N, "Bada")        :- 0 is N mod 3, \+ 0 is N mod 5.
badaboom(N, "Boom!!")      :- 0 is N mod 5, \+ 0 is N mod 3.
badaboom(N, N)             :- \+ 0 is N mod 3, \+ 0 is N mod 5.

%%R007%%
%%15%%
/*
Bada Boom!! Parte 2
*/
lista_badaboom(0, []) :- !.
lista_badaboom(N, L) :-
    N > 0,
    N1 is N - 1,
    lista_badaboom(N1, L1),
    badaboom(N, R),
    append(L1, [R], L).

%%R008%%
%%20%%
/*
Mapa del tesoro
*/
pirata([], PX, PY, PX, PY).
pirata(["A"|R], PX, PY, RX, RY) :- PY1 is PY+1, pirata(R, PX, PY1, RX, RY).
pirata(["V"|R], PX, PY, RX, RY) :- PY1 is PY-1, pirata(R, PX, PY1, RX, RY).
pirata([">"|R], PX, PY, RX, RY) :- PX1 is PX+1, pirata(R, PX1, PY, RX, RY).
pirata(["<"|R], PX, PY, RX, RY) :- PX1 is PX-1, pirata(R, PX1, PY, RX, RY).

%%R009%%
%%10%%
/*
Combinar listas
*/
combina_listas([], [], []).
combina_listas([], L2, L2) :- L2 \= [].
combina_listas(L1, [], L1) :- L1 \= [].
combina_listas([F|C], [G|D], [F,G|R]) :-
    combina_listas(C, D, R).

