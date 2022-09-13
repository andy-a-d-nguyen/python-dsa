# Efficiency

- Efficiency: A measure of the use of computing resources by code
  - Can be relative to speed (runtime), memory (space), etc.
  - Most commonly refers to runtime
- To examine program runtime, let's assume:
  - A single statement's runtime = 1
  - A function call's runtime = sum of runtime of statements in function's body
  - A loop of N iterations' runtime = N * loop body's runtime

## Efficiency Example

```c++
statement1;                         // runtime = 1

for (int i = 1; i <= N; i++) {      // runtime = N ^ 2
    for (int j = 1; j <= N; j++) {  // runtime = N
        statement2;
    }
}

for (int i = 1; i <= N; i++) {      // runtime = 3N
    statement3;
    statement4;
    statement5;
}
                                    // total = N^2 + 3N + 1
```

## Algorithm Growth Rates

- Growth rate: Change in runtime as input size "N" changes
- Say an algorithm runs 0.4N^3 + 25N^2 + 8N + 17
  - We ignore constants like 25 because they are tiny next to N
  - The highest-order term (N^3) dominates the overall runtime
    - This is especially true when N is extremely large
    - The other terms (25N^2 + 8N + 17) don't matter and are ignored
  - We say this algorithm executes "on the order of N^3" statements
  - Or O(N^3) for short

## Vector Efficiency

| Member                 | Big O |
|------------------------|-------|
| v.add(value)           | O(1)  |
| v.get(i) or v[i]       | O(1)  |
| v.insert(i, value)     | O(N)  |
| v.remove(i)            | O(N)  |
| v.set(i, val) or v[i]= | O(1)  |
| v.size(), v.isEmpty()  | O(1)  |
| v.toString()           | O(N)  |

## Complexity Classes

- Complexity class: A category of algorithm efficiency based on the algorithm's relationship to the input size "N"

| Class       | Big O         | If you double N, ...         |
|-------------|---------------|------------------------------|
| constant    | O(1)          | unchanged                    |
| logarithmic | O(log2 N)     | increases slightly           |
| linear      | O(N)          | doubles                      |
| log-linear  | O(N log2 N)   | slightly more than doubles   |
| quadratic   | O(N^2)        | quadruples                   |
| quad-linear | O(N^2 log2 N) | slightly more than quadruple |
| cubic       | O(N^3)        | multiplies by 8              |
| exponential | O(2^N)        | multiplies drastically       |
| factorial   | O(N!)         | multiplies drastically       |
