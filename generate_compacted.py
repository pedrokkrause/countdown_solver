import string
from fractions import Fraction
from random import randint
from collections import defaultdict
from itertools import permutations

n = 6

variables = tuple(string.ascii_lowercase[:n])
operations = tuple('+-*/')
right_par = (')',)
left_par = ('(',)
after_variables = operations + right_par
ops_left_par = operations + left_par
empty = tuple()

def build_lambda(expression):
    return eval(f"lambda {','.join(variables)}: {expression}")

def next_symbols_allowed(expression, var_idx=0, opened_pars=0, unused_pars=(True,)):
    if var_idx < n:
        next_var = (variables[var_idx],)

    if not expression:
        return next_var + left_par

    last_char = expression[-1]
    required_vars = (sum(unused_pars)+1) * 2

    if last_char.isalpha():
        if var_idx < n:
            if unused_pars[-1] or opened_pars == 0:
                return operations
            else:
                return after_variables
        else:
            if opened_pars == 0:
                return empty
            else:
                return right_par
    elif last_char in ops_left_par:
        if required_vars > n-var_idx:
            return next_var
        else:
            return next_var + left_par
    elif last_char == ')':
        if var_idx < n:
            if opened_pars == 0 or required_vars > n-var_idx:
                return operations
            else:
                return after_variables
        else:
            if opened_pars == 0:
                return empty
            else:
                return right_par

expressions = []

def search(expression='', var_idx=0, opened_pars=0, unused_pars=(True,)):
    allowed_chars = next_symbols_allowed(expression, var_idx, opened_pars, unused_pars)

    if opened_pars == 0 and not any(unused_pars) and not (expression[-1] in operations):
        func = build_lambda(expression)
        expressions.append((expression, func))

    for symbol in allowed_chars:
        new_expression = expression + symbol
        if symbol.isalpha():
            search(new_expression, var_idx+1, opened_pars, unused_pars)
        elif symbol in operations:
            search(new_expression, var_idx, opened_pars, unused_pars[:-1]+(False,))
        elif symbol == '(':
            search(new_expression, var_idx, opened_pars+1, unused_pars+(True,))
        elif symbol == ')':
            search(new_expression, var_idx, opened_pars-1, unused_pars[:-1])

search()
print(len(expressions))

"""
Filter the expressions that produce the same result, keeping the one with the least parenthesis
"""

values = tuple(Fraction(randint(100000, 1000000), randint(100000, 1000000)) for _ in range(n))

possible_results = defaultdict(lambda: [])
for item in expressions:
    f = item[1]
    x = f(*values)
    possible_results[x].append(item)

expressions = []
for v in possible_results.values():
    best_expression = min(v, key=lambda x: x[0].count('('))
    expressions.append(best_expression)

print(len(expressions))

"""
Filter the expressions that produce the same result over some permutation
"""

possible_results = defaultdict(lambda: [])

for p in permutations(values):
    for exp, f in expressions:
        val = f(*p)
        possible_results[val].append(exp)

seen = set()
expressions = set()
for exps in possible_results.values():
    fresh = [e for e in exps if e not in seen]
    if not fresh:
        continue
    expressions.add(fresh[0])
    seen.update(exps)

print(len(expressions))

with open('compacted_expressions.txt', 'w') as f:
    for exp in expressions:
        f.write(f'{exp}\n')