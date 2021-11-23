% Bryan John Baker
% CSCI 5511
% Homework 7 - First-Order Logic: Prolog

% Kinship Domain
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
