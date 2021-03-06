%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Bryan John Baker
% CSCI 5511
% Homework 7 - First-Order Logic: Prolog
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Kinship Domain
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% These are given.
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
% Y is the parent of X implies that X is a child of Y.
child(X, Y) :- parent(Y, X).

% Define the sibling predicate
% P is the parent of X and the parent of Y where X and Y are 
%      different people implies that X and Y are siblings.
sibling(X, Y) :- parent(P, X), parent(P, Y), not(X=Y).

% Define the cousin predicate
% A is the parent of X and B is the parent of Y where A and B are 
%      siblings implies that X and Y are cousins.
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B), not(A=B).

% Define the ancestor predicate
% As a base case X is the parent of Z implies that X is an ancestor of Z.
%      To go further back: Y is a parent of Z and X is an ancestor of Y 
%      implies that X is an ancestor of Z.
ancestor(X, Z) :- parent(X, Z).
ancestor(X, Z) :- parent(Y, Z), ancestor(X, Y).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Basic Length Definition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is given as an example.
len([], 0).
len([_ | T], N) :- len(T, M), N is M+1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Sorted predicate
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
sorted([]).  % base case stating that the empty list is sorted.
sorted([_]).  % base case stating that a list with one element is sorted.
% If the first element of the list is less than or equal to the second element  
%      and the list without the first element is sorted this implies that the larger
%      list is sorted.
sorted([H, A | T]) :- H =< A, sorted([A|T]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Perm predicate 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% My initial perm statement was much longer so I created this function.  
% I will just leave this here.
is_in(X, [H|_]) :- X = H.
is_in(X, [_|T]) :- is_in(X, T).

% This function is needed to help make the two lists in the perm function smaller 
%     by removing the same element.
% Base case: if the item to remove is the first item in the list then return the rest of the list.
remove_item(A, [A|B], B).
% if the item to remove is not the first item in the list then it is implied that we can add an 
%     element to the beginning of the lists without worrying about the item.
remove_item(A, [B|C], [B|D]) :- remove_item(A, C, D).

% This is the perm function.
% Base case: if the two lists to compare are both empty then this is true.
perm([],[]).
% Removing the first element from the first list and the same element from the second list where the resulting two shorter
%     lists are permutations implies that the two larger lists are permutations.
perm([H1|T1], [H2|T2]) :- 
    remove_item(H1, [H2|T2], Y), 
    perm(T1, Y).

% Note: I had a test that the lengths for the two lists should be equal, but this did not allow for the permutations to 
%          be generated for the sort function next so I had to rewrite this.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Mysort predicate 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% If permutations are generated from a list of values and that permutated list is sorted then that implies that the 
%       list we are looking for is sorted.
mysort(L, M) :- perm(M, L), sorted(M), !.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Mysort time complexity
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% I collected data for the number of list elements (n) and the time required to complete the sort.
% For the time I used: time(mysort(L, M)). For example.
% X = [6, 7, 8, 9, 10, 11, 12] % Number of elements in the list.
% Y = [0.002, 0.007, 0.042, 0.298, 2.918, 32.292, 391.229] % Time in seconds to complete the sort.
% Plotting the X data as n! and putting both X and Y on a log-log scale shows a straight line suggesting the sort is O(n!).

% To determine the time complexity of mysort we need to analyze the functions that make it up.
% First the sorted function:
% This function gets called continuously on a list with one less element each time therefore the 
%     time complexity is O(n).
% Next the perm function:
% This function generates lists that the sorted function tests.  
%     All possible permutations of the list are generated for a max number of n!.
% When both of these functions are combined to create the mysort function 
%     in the worst case the mysort function will find a sorted list for 
%     the last list generated by the perm function.  The time to generate all permutations out weighs the
%     time to check the list is sorted.
%     Therefore the time complexity for the mysort function is: O(n!).
%     This agrees with the data that was collected.
