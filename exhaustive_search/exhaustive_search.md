# Exhaustive Search

- Exhaustive Search: Exploring every possible combination from a set of choice or values
  - Often implemented recursively
- Applications:
  - Producing all permutations of a set of values
  - Enumerating all possible names, passwords, etc.
  - Combinatorics and logic programming
- Often the search space consists of many decisions, each of which has several choices
  - Example: When enumerating all 5-letter strings, each of the 5 letters is a decision, and each of those decisions has
26 possible choices

A general pseudocode algorithm for exhaustive search:
- If there are no more decisions to make: Stop
- Else, let's handle one decision ourselves, and the rest by recursion for each available choice C for this decision:
  - Choose C
  - Explore the remaining decisions that could follow C

## Helper Functions

- If the required function doesn't accept the parameters you need:
  - Write a helper function that accepts more parameters
  - Extra parameters can represent current state, choices made, etc
  - helper params can be used as accumulators

```python
def function_name(params):
    return helper(params, more_params)

def helper(params, more_params):
    ...
```