% This doesn't work.  

init(3,2,46).
init(4,2,45).
init(6,2,55).
init(7,2,74).
init(2,3,38).
init(8,3,78).
init(2,4,35).
init(8,4,71).
init(3,5,33).
init(7,5,59).
init(2,6,17).
init(8,6,67).
init(2,7,18).
init(5,7,11).
init(8,7,64).
init(3,8,24).
init(4,8,21).
init(6,8,1).
init(7,8,2).

append([X|Y],Z,[X|W]) :- append(Y,Z,W).
append([],X,X).

move(OldX,OldY,NewX,NewY) :- 
    NewY is OldY + 1,
    NewY < 10,
    NewY > -1,
    NewX is OldX,
    NewX < 10,
    NewX > -1.

move(OldX,OldY,NewX,NewY) :- 
    NewY is OldY,
    NewY < 10,
    NewY > -1,
    NewX is OldX + 1,
    NewX < 10,
    NewX > -1.

move(OldX,OldY,NewX,NewY) :- 
    NewY is OldY - 1,
    NewY < 10,
    NewY > -1,
    NewX is OldX,
    NewX < 10,
    NewX > -1.

move(OldX,OldY,NewX,NewY) :- 
    NewY is OldY,
    NewY < 10,
    NewY > -1,
    NewX is OldX - 1,
    NewX < 10,
    NewX > -1.

member(X,[X|_]).
member(X,[H|R]) :- member(X,R).
/*
path([A],[B],[1]) :- init(A,B,1).
% path([],[],[]) :- path([6],[8],[1]).
% path([Xhead | [OldX | X]],[Yhead | [OldY | Y]],[Lhead | [OldL | L]]) :- Lhead is OldL + 1, move(OldX,OldY,Xhead,Yhead), init(Xhead,Yhead,Lhead).

% path(Z,Z,L).

% path([Xhead | [OldX]],[Yhead | [OldY]],[Lhead | [1]]) :- path([OldX],[OldY],[1]), move(OldX,OldY,Xhead,Yhead), Lhead is 2, init(Xhead,Yhead,Lhead).
path([Xhead | [OldX]],[Yhead | [OldY]],[Lhead | [1]]) :-
    Lhead is 2,
    move(OldX,OldY,Xhead,Yhead),
    init(Xhead,Yhead,Lhead),
    path([OldX],[OldY],[1]).
% path([Xhead | [OldX]],[Yhead | [OldY]],[Lhead | [1]]) :- path([OldX],[OldY],[1]), move(OldX,OldY,Xhead,Yhead), Lhead is 2.
% path([Xhead | [OldX | X]],[Yhead | [OldY | Y]],[Lhead | [OldL | L]]) :- path([OldX | X],[OldY | Y],[OldL|L]), move(OldX,OldY,Xhead,Yhead), init(OldX,OldY,OldL), Lhead is OldL + 1.
% path([Xhead | [OldX | X]],[Yhead | [OldY | Y]],[Lhead | [OldL | L]]) :- path([OldX | X],[OldY | Y],[OldL|L]), move(OldX,OldY,Xhead,Yhead), Lhead is OldL + 1.
path([Xhead | [OldX | X]],[Yhead | [OldY | Y]],[Lhead | [OldL | L]]) :- 
    Lhead is OldL + 1, 
    move(OldX,OldY,Xhead,Yhead), 
    init(Xhead,Yhead,Lhead), 
    path([OldX | X], [OldY | Y], [OldL | L]).
*/

path([A], [B], [1], 1) :- init(A, B, 1).
path([NewX | [OldX | X]], [NewY | [OldY | Y]], [C | [C1 | L]], C) :- 
    path([OldX | X], [OldY | Y], [C1 | L], C1),
    C is C1 + 1,
    move(OldX, OldY, NewX, NewY),
    init(NewX, NewY, C).
path([NewX | [OldX | X]], [NewY | [OldY | Y]], [C | [C1 | L]], C) :- 
    path([OldX | X], [OldY | Y], [C1 | L], C1),
    C is C1 + 1,
    move(OldX, OldY, NewX, NewY).

