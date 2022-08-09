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

function Explore(decisions):
- If there are decisions left to make:
  - Let's handle one decision ourselves, and the rest by recursion
  - For each available choice C in my decision:
    - Choose C
    - Explore the remaining decisions that could follow C
    - Un-choose C (backtrack)
- Otherwise, if there are no more decisions to make: Stop

- Key tasks:
  - Figure out appropriate smallest unit of work (decision)
  - Figure out how to enumerate all possible choices/options for it

## "Arm's Length" Recursion

- Arm's length recursion: A poor style where unnecessary tests are performed before performing recursive calls.
  - Typically, the tests try to avoid making a call into what would otherwise be a base case
- Example: escape_maze
  - The code recursively tries to explore up, down, left, and right
  - Some of those directions may lead to walls or off the board. Shouldn't we test before making calls in these 
    directions?

Essentially, arm's length recursion is excessively checking for bad paths before making recursive calls. This fills up 
the code with unnecessary conditional checks as opposed to making recursive calls to check for bad paths.

## 8 Queens

### Naive algorithm

For (each board square):
- Place a queen there
- Try to place the rest of the queens
- Un-place the queen

### Better algorithm idea

- Observation: In a working solution, exactly 1 queen must appear in each row and in each column
  - Redefine a "choice" to be valid placement of a queen in a particular column
