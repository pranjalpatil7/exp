%  FACTS 

% Gender Information
male(husband).
male(brother).
male(son).

female(alice).
female(daughter).

% Relationships
twin(brother, alice).
twin(alice, brother).
twin(son, daughter).
twin(daughter, son).

child(son).
child(daughter).

% Locations on the Night of the Murder (Clue)

not_together(husband, alice).

on_beach(alice).
on_beach(brother).

in_bar(husband).
in_bar(daughter).

younger(alice, brother).

alone(son).

% RULES (Logical Inference)

% Rule 1: A pair were together on the beach
together_on_beach(X, Y) :-
    on_beach(X),
    on_beach(Y),
    X \= Y.

% Rule 2: The victim was a twin
victim(Y) :-
    twin(Y, _),
    on_beach(Y).

% Rule 3: The killer is younger than the victim
younger_than(X, Y) :-
    younger(X, Y).

% Rule 4: The killer must satisfy all clues
killer(X) :-
    victim(Y),
    together_on_beach(X, Y),
    younger_than(X, Y),
    not_together(husband, alice),
    alone(son),
    male(husband),
    female(alice).

% ?- killer(K), victim(V).

% Expected Output:
% K = alice,
% V = brother.
