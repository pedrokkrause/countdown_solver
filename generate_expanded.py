import string
from itertools import permutations
from collections import defaultdict
from fractions import Fraction
from random import randint

n = 6
variables = string.ascii_lowercase[:n]

compacted_expressions = []
with open('compacted_expressions.txt', 'r') as f:
    for line in f:
        compacted_expressions.append(line.strip())

expanded_expressions = []
for p in list(permutations(variables)):
    trans = str.maketrans(variables, ''.join(p))
    for exp in compacted_expressions:
        new_exp = exp.translate(trans)
        expanded_expressions.append(new_exp)

funcs = tuple(eval(f"lambda {','.join(variables)}: {expression}") for expression in expanded_expressions)

values = tuple(Fraction(randint(100000, 1000000), randint(100000, 1000000)) for _ in range(n))

possible_results = defaultdict(lambda: [])
for f,exp in zip(funcs, expanded_expressions):
    val = f(*values)
    possible_results[val].append(exp)

seen = set()
expanded_expressions = set()

for exps in possible_results.values():
    fresh = [e for e in exps if e not in seen]
    if not fresh:
        continue
    expanded_expressions.add(fresh[0])
    seen.update(exps)

print(len(expanded_expressions))

with open('expanded_expressions.txt', 'w') as f:
    for expr in expanded_expressions:
        f.write(f'{expr}\n')