%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Bryan John Baker
% CSCI 5511
% Homework 7 - First-Order Logic: Prolog
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Kinship Domain
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
parent(charles, william).
parent(charles, harry).
parent(elizabeth, charles).
parent(george, elizabeth).
parent(george, margaret).
parent(elizabeth, anne).
parent(elizabeth, andrew).
parent(elizabeth, edward).
parent(anne, peter).
parent(anne, zara).
parent(andrew, beatrice).
parent(andrew, eugenie).
parent(edward, louise).
parent(edward, james).

% Define the child predicate
child(X, Y) :- parent(Y, X).

% Define the sibling predicate
sibling(X, Y) :- parent(P, X), parent(P, Y), not(X=Y).

% Define the cousin predicate
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B), not(A=B).

% Define the ancestor predicate
ancestor(X, Z) :- parent(X, Z).
ancestor(X, Z) :- parent(Y, Z), ancestor(X, Y).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Basic Length Definition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
len([], 0).
len([_ | T], N) :- len(T, M), N is M+1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Sorted predicate
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
sorted([]).
sorted([_]).
sorted([H, A | T]) :- H =< A, sorted([A|T]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Perm predicate 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
is_in(X, [H|_]) :- X = H, !.
is_in(X, [_|T]) :- is_in(X, T).

remove_item(A, [A|B], B).
remove_item(A, [B|C], [B|D]) :- remove_item(A, C, D).

perm([],[]).
perm([H1|T1], [H2|T2]) :- 
    len([H1|T1], X), 
    len([H2|T2], X), 
    is_in(H1, [H2|T2]), 
    is_in(H2, [H1|T1]), 
    remove_item(H1, [H2|T2], Y), 
    perm(Y, T1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Mysort predicate 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Mysort time complexity
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
