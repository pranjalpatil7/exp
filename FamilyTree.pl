% FACTS

% Gender
male(john).
male(michael).
male(david).
male(chris).
male(sam).

female(linda).
female(susan).
female(karen).
female(emma).
female(sophia).

% Parent relationships
parent(john, michael).
parent(linda, michael).

parent(john, susan).
parent(linda, susan).

parent(michael, david).
parent(karen, david).

parent(michael, emma).
parent(karen, emma).

parent(susan, chris).
parent(sam, chris).

parent(susan, sophia).
parent(sam, sophia).

% RULES

% Father rule
father(X, Y) :- male(X), parent(X, Y).

% Mother rule
mother(X, Y) :- female(X), parent(X, Y).

% Sibling rule
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Grandparent rule
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Grandfather rule
grandfather(X, Y) :- male(X), grandparent(X, Y).

% Grandmother rule
grandmother(X, Y) :- female(X), grandparent(X, Y).

% Uncle rule
uncle(X, Y) :- male(X), sibling(X, Z), parent(Z, Y).

% Aunt rule
aunt(X, Y) :- female(X), sibling(X, Z), parent(Z, Y).

% Cousin rule
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B), X \= Y.

% Query 
% father(X, david). ---> X = michael.
% sibling(susan, X). ---> X = michael.
% grandmother(X, emma). ---> X = linda.
% uncle(X, sophia). ---> X = michael.
% mother(linda, susan). ---> true
% sibling(david, emma). ---> true
% aunt(X, david). ---> X = susan

%                    ┌──────────────┐
%                    │   John (M)   │───┐
%                    └──────────────┘   │
%                                        │
%                    ┌──────────────┐    │
%                    │  Linda (F)   │────┘
%                           │
%          ┌────────────────┴────────────────┐
%          │                                 │
%  ┌──────────────┐                  ┌──────────────┐
%  │ Michael (M)  │                  │  Susan (F)   │
%  └──────────────┘                  └──────────────┘
%        │                                 │
%  ┌──────────────┐                  ┌──────────────┐
%  │  Karen (F)   │                  │   Sam (M)    │
%  └──────────────┘                  └──────────────┘
%        │                                 │
%    ┌────┴─────┐                     ┌────┴─────┐
%    │          │                     │          │
% ┌──────┐  ┌──────┐             ┌──────┐   ┌────────┐
% │David │  │Emma  │             │Chris │   │Sophia │
% └──────┘  └──────┘             └──────┘   └────────┘
