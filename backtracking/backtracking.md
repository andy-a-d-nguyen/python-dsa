# Backtracking

- Backtracking: Finding solution(s) by trying partial solutions and then abandoning the if they are not suitable
  - A "brute force" algorithmic technique (tries all paths)
  - often implemented recursively
- Applications:
  - Producing all permutations of a set of values
  - Parsing languages
  - Games: anagrams, crosswords, word jumbles, 8 queens
  - Combinatorics and logic programming
  - Escape from a maze

## A general pseudocode algorithm for backtracking problems

Explore(decisions):
- If there are no more decisions to make: stop
- Else, Let's handle one decision ourselves, and the rest by recursion. For each available choice C for this decision:
  - Choose C
  - Explore the remaining decisions that could follow C
  - Un-choose C (backtrack)