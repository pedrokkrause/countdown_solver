# Countdown Solver

This project provides a solver for the game **Countdown** based on generating and evaluating all possible arithmetic expressions that can be formed from a set of six numbers, using the operations `+`, `-`, `*`, and `/`. The goal is to reach a target number (or get as close as possible).

## How It Works

* **Compacted Expressions:**
  The minimal set of expressions needed to generate every possible outcome from the given numbers. To solve a problem, every permutation of the numbers (6! = 720) is tested against each of the 3,444 compacted expressions, totaling 2,479,680 evaluations per problem.

* **Expanded Expressions:**
  All possible permutations are applied to the compacted expressions, generating over 2 million possibilities, which are then filtered down to 970,324 unique expressions (a reduction factor of 2.55). This provides a fully expanded set for exhaustive solving.

## Solvers

* **Compacted Solver (`c_solver.py`):**
  Loads the compacted expressions and evaluates every permutation of the numbers with each expression. This method is recommended for most use cases due to its efficiency.

* **Expanded Solver (`e_solver.py`):**
  Loads the expanded set of expressions and tests each one against the input numbers in their original order. This is more exhaustive but significantly slower to load and run.

## Hard Problem Finder

The `hard_problems_finder.py` script searches for especially challenging Countdown instances—those with an exact solution but where all other expressions are as far from the target as possible.

**The hardest problem found so far is:**

```
Numbers: 28, 74, 6, 73, 1, 47
Target: 984
```

## File Overview

* `generate_compacted.py`: Generates the compacted expression set.
* `generate_expanded.py`: Expands permutations and filters for unique expressions.
* `c_solver.py`: Solver using compacted expressions (efficient, recommended).
* `e_solver.py`: Solver using expanded expressions (comprehensive, slower).
* `hard_problems_finder.py`: Finds especially hard problems.
