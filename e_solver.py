import pickle
import string
from itertools import permutations
from time import perf_counter

alphabet = string.ascii_lowercase
n = 6
variables = tuple(alphabet[:n])

expressions = []
with open('expanded_expressions.txt','r') as f:
    for line in f:
        expressions.append(line.strip())
print(f"{len(expressions)} expressions loaded")

funcs = tuple(eval(f"lambda {','.join(variables)}: {expression}") for expression in expressions)

numbers = (25,50,100,6,9,5)
target = 857

def insert_values(expression, numbers):
    new_expression = expression
    for char, num in zip(variables,numbers):
        new_expression = new_expression.replace(char, str(num))
    return new_expression

best_error = float('inf')
best_expression = None

t0 = perf_counter()
tries = 0
for (f,exp) in zip(funcs, expressions):
    try:
        val = f(*numbers)
    except ZeroDivisionError:
        continue
    tries += 1
    error = abs(val - target)
    if error <= best_error:
        best_error = error
        best_expression = exp
        t1 = perf_counter()
        print(f"{tries}\t{insert_values(exp, numbers)}\t{best_error}\t{t1 - t0:.6f}")

t1 = perf_counter()
print(tries, t1-t0)