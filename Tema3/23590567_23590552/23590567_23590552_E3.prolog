% Examen 3

% Jose Luis Acosta Garcia 23590567
% Luis Carlos Cuellar Trejo 23590552

% =========================================================================
% ##R001## (50 pts): Árbol Genealógico y Parentescos
% =========================================================================

yerno(Ego, Persona) :- 
    sucesor(Persona, Hija), 
    (pareja(Hija, Ego); pareja(Ego, Hija)).

bisnieto_a(Bisabuelo, Bisnieto) :- 
    sucesor(Bisabuelo, Abuelo), 
    sucesor(Abuelo, Padre), 
    sucesor(Padre, Bisnieto).

sobrino_a_nieto(Ego, Persona) :- 
    hermano(Persona, Hermano), 
    sucesor(Hermano, Hijo), 
    sucesor(Hijo, Ego).
sobrino_a_nieto(Ego, Persona) :- 
    pareja(Persona, Pareja), 
    hermano(Pareja, Hermano), 
    sucesor(Hermano, Hijo), 
    sucesor(Hijo, Ego).
sobrino_a_nieto(Ego, Persona) :- 
    pareja(Pareja, Persona), 
    hermano(Pareja, Hermano), 
    sucesor(Hermano, Hijo), 
    sucesor(Hijo, Ego).

abuelo_a(Abuelo, Nieto) :- 
    sucesor(Abuelo, Padre), 
    sucesor(Padre, Nieto).

tio_bisabuelo_a(Tio_bisabuelo, Bisnieto) :- 
    hermano(Tio_bisabuelo, Bisabuelo), 
    bisnieto_a(Bisnieto, Bisabuelo).
tio_bisabuelo_a(Tio_bisabuelo, Bisnieto) :- 
    hermano(Bisabuelo, Tio_bisabuelo), 
    bisnieto_a(Bisnieto, Bisabuelo).


% =========================================================================
% ##R002## (20 pts): Descendiente
% =========================================================================

descendiente(EGO, PERSONA2) :- 
    sucesor(PERSONA2, EGO).
descendiente(EGO, PERSONA2) :- 
    sucesor(PERSONA2, X), 
    descendiente(EGO, X).


% =========================================================================
% ##R003## (20 pts): Todos los descendientes con findall
% =========================================================================

descendientes(EGO, ListaDESCENDIENTES) :-
    findall(Descendiente, descendiente(Descendiente, EGO), ListaDESCENDIENTES).

%set_prolog_flag(answer_write_options,[max_depth(0)])

% Parejas
pareja(monsieur_delacour, apolline_delacour).
pareja(bill_weasley, fleur_isabelle_delacour).
pareja(percy_weasley, audrey_weasley).
pareja(george_weasley, angelina_johnson).
pareja(ron_weasley, hermione_granger).
pareja(harry_james_potter, ginny_weasley).
pareja(arthur_weasley, molly_prewett).
pareja(james_potter, lily_evans).
pareja(vernon_dursley, petunia_evans).
pareja(dudley_dursley, wife_dursley).
pareja(xenophilius_lovegood, pandora_lovegood).
pareja(rolf_scamander, luna_lovegood).
pareja(orion_black, walburga_black).
pareja(frank_longbottom, alice_longbottom).
pareja(neville_longbottom, hannah_abbot).
pareja(cygnus_black_iii, druella_rosier).
pareja(rodolphus_lestrange, bellatrix_black).
pareja(ted_tonks, andromeda_black).
pareja(remus_lupin, nymphadora_tonks).
pareja(lucius_malfoy, narcisa_black).
pareja(draco_lucius_malfoy, astoria_greengrass).
pareja(victoire_weasley, teddy_remus_lupin).

% Hermanos
hermano(gabrielle_delacour, fleur_isabelle_delacour).
hermano(fleur_isabelle_delacour, gabrielle_delacour).
hermano(lily_evans, petunia_evans).
hermano(petunia_evans, lily_evans).
hermano(vernon_dursley, marjorie_eileen_dursley).
hermano(marjorie_eileen_dursley, vernon_dursley).
hermano(son1_dursley, son2_dursley).
hermano(son2_dursley, son1_dursley).
hermano(astoria_greengrass, daphne_greengrass).
hermano(daphne_greengrass, astoria_greengrass).
hermano(walburga_black, cygnus_black_iii).
hermano(cygnus_black_iii, walburga_black).

hermano(bill_weasley, charlie_weasley).
hermano(charlie_weasley, bill_weasley).
hermano(bill_weasley, percy_weasley).
hermano(percy_weasley, bill_weasley).
hermano(bill_weasley, fred_weasley).
hermano(fred_weasley, bill_weasley).
hermano(bill_weasley, george_weasley).
hermano(george_weasley, bill_weasley).
hermano(bill_weasley, ron_weasley).
hermano(ron_weasley, bill_weasley).
hermano(bill_weasley, ginny_weasley).
hermano(ginny_weasley, bill_weasley).

hermano(charlie_weasley, percy_weasley).
hermano(percy_weasley, charlie_weasley).
hermano(charlie_weasley, fred_weasley).
hermano(fred_weasley, charlie_weasley).
hermano(charlie_weasley, george_weasley).
hermano(george_weasley, charlie_weasley).
hermano(charlie_weasley, ron_weasley).
hermano(ron_weasley, charlie_weasley).
hermano(charlie_weasley, ginny_weasley).
hermano(ginny_weasley, charlie_weasley).

hermano(percy_weasley, fred_weasley).
hermano(fred_weasley, percy_weasley).
hermano(percy_weasley, george_weasley).
hermano(george_weasley, percy_weasley).
hermano(percy_weasley, ron_weasley).
hermano(ron_weasley, percy_weasley).
hermano(percy_weasley, ginny_weasley).
hermano(ginny_weasley, percy_weasley).

hermano(fred_weasley, george_weasley).
hermano(george_weasley, fred_weasley).
hermano(fred_weasley, ron_weasley).
hermano(ron_weasley, fred_weasley).
hermano(fred_weasley, ginny_weasley).
hermano(ginny_weasley, fred_weasley).

hermano(george_weasley, ron_weasley).
hermano(ron_weasley, george_weasley).
hermano(george_weasley, ginny_weasley).
hermano(ginny_weasley, george_weasley).

hermano(ron_weasley, ginny_weasley).
hermano(ginny_weasley, ron_weasley).

hermano(victoire_weasley, dominique_weasley).
hermano(dominique_weasley, victoire_weasley).
hermano(victoire_weasley, louis_weasley).
hermano(louis_weasley, victoire_weasley).
hermano(dominique_weasley, louis_weasley).
hermano(louis_weasley, dominique_weasley).

hermano(molly_weasley_ii, lucy_weasley).
hermano(lucy_weasley, molly_weasley_ii).

hermano(fred_weasley_ii, roxanne_weasley).
hermano(roxanne_weasley, fred_weasley_ii).

hermano(rose_granger_weasley, hugo_granger_weasley).
hermano(hugo_granger_weasley, rose_granger_weasley).

hermano(james_sirius_potter, albus_severus_potter).
hermano(albus_severus_potter, james_sirius_potter).
hermano(james_sirius_potter, lily_luna_potter).
hermano(lily_luna_potter, james_sirius_potter).
hermano(albus_severus_potter, lily_luna_potter).
hermano(lily_luna_potter, albus_severus_potter).

hermano(lysander_scamander, lorcan_scamander).
hermano(lorcan_scamander, lysander_scamander).

hermano(bellatrix_black, andromeda_black).
hermano(andromeda_black, bellatrix_black).
hermano(bellatrix_black, narcisa_black).
hermano(narcisa_black, bellatrix_black).
hermano(andromeda_black, narcisa_black).
hermano(narcisa_black, andromeda_black).

hermano(sirius_black, regulus_arcturus_black).
hermano(regulus_arcturus_black, sirius_black).

% Sucesores
sucesor(apolline_delacour, fleur_isabelle_delacour).
sucesor(apolline_delacour, gabrielle_delacour).
sucesor(monsieur_delacour, fleur_isabelle_delacour).
sucesor(monsieur_delacour, gabrielle_delacour).

sucesor(bill_weasley, victoire_weasley).
sucesor(bill_weasley, dominique_weasley).
sucesor(bill_weasley, louis_weasley).
sucesor(fleur_isabelle_delacour, victoire_weasley).
sucesor(fleur_isabelle_delacour, dominique_weasley).
sucesor(fleur_isabelle_delacour, louis_weasley).

sucesor(percy_weasley, molly_weasley_ii).
sucesor(percy_weasley, lucy_weasley).
sucesor(audrey_weasley, molly_weasley_ii).
sucesor(audrey_weasley, lucy_weasley).

sucesor(george_weasley, fred_weasley_ii).
sucesor(george_weasley, roxanne_weasley).
sucesor(angelina_johnson, fred_weasley_ii).
sucesor(angelina_johnson, roxanne_weasley).

sucesor(ron_weasley, rose_granger_weasley).
sucesor(ron_weasley, hugo_granger_weasley).
sucesor(hermione_granger, rose_granger_weasley).
sucesor(hermione_granger, hugo_granger_weasley).

sucesor(harry_james_potter, lily_luna_potter).
sucesor(harry_james_potter, james_sirius_potter).
sucesor(harry_james_potter, albus_severus_potter).
sucesor(ginny_weasley, lily_luna_potter).
sucesor(ginny_weasley, james_sirius_potter).
sucesor(ginny_weasley, albus_severus_potter).

sucesor(arthur_weasley, bill_weasley).
sucesor(arthur_weasley, charlie_weasley).
sucesor(arthur_weasley, percy_weasley).
sucesor(arthur_weasley, fred_weasley).
sucesor(arthur_weasley, george_weasley).
sucesor(arthur_weasley, ron_weasley).
sucesor(arthur_weasley, ginny_weasley).
sucesor(molly_prewett, bill_weasley).
sucesor(molly_prewett, charlie_weasley).
sucesor(molly_prewett, percy_weasley).
sucesor(molly_prewett, fred_weasley).
sucesor(molly_prewett, george_weasley).
sucesor(molly_prewett, ron_weasley).
sucesor(molly_prewett, ginny_weasley).

sucesor(james_potter, harry_james_potter).
sucesor(lily_evans, harry_james_potter).

sucesor(vernon_dursley, dudley_dursley).
sucesor(petunia_evans, dudley_dursley).
sucesor(dudley_dursley, son1_dursley).
sucesor(dudley_dursley, son2_dursley).
sucesor(wife_dursley, son1_dursley).
sucesor(wife_dursley, son2_dursley).

sucesor(xenophilius_lovegood, luna_lovegood).
sucesor(pandora_lovegood, luna_lovegood).
sucesor(rolf_scamander, lysander_scamander).
sucesor(rolf_scamander, lorcan_scamander).
sucesor(luna_lovegood, lysander_scamander).
sucesor(luna_lovegood, lorcan_scamander).

sucesor(orion_black, sirius_black).
sucesor(orion_black, regulus_arcturus_black).
sucesor(walburga_black, sirius_black).
sucesor(walburga_black, regulus_arcturus_black).

sucesor(frank_longbottom, neville_longbottom).
sucesor(alice_longbottom, neville_longbottom).

sucesor(cygnus_black_iii, bellatrix_black).
sucesor(cygnus_black_iii, narcisa_black).
sucesor(cygnus_black_iii, andromeda_black).
sucesor(druella_rosier, bellatrix_black).
sucesor(druella_rosier, narcisa_black).
sucesor(druella_rosier, andromeda_black).

sucesor(ted_tonks, nymphadora_tonks).
sucesor(andromeda_black, nymphadora_tonks).
sucesor(remus_lupin, teddy_remus_lupin).
sucesor(nymphadora_tonks, teddy_remus_lupin).

sucesor(lucius_malfoy, draco_lucius_malfoy).
sucesor(narcisa_black, draco_lucius_malfoy).
sucesor(draco_lucius_malfoy, scorpius_hyperion_malfoy).
sucesor(astoria_greengrass, scorpius_hyperion_malfoy).

sucesor(victoire_weasley, hijo_victoire_teddy).
sucesor(teddy_remus_lupin, hijo_victoire_teddy).


% =========================================================================
% ##R004## (10 pts): Secuencia matemática
% =========================================================================

seq0(0, 7). 
seq0(N, R) :- 
    NN is N - 1, 
    seq0(NN, RR), 
    R is 2 * RR + 3.


% =========================================================================
% ##R005## (35 pts): Recorrido en un grafo circular
% =========================================================================

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
    write(Limite), nl.
imp_graf_cir(Inicio, Limite) :- 
    Inicio \== Limite, 
    write(Inicio), nl, 
    grafo(Inicio, Sig), 
    imp_graf_cir(Sig, Limite).