import pickle
import string
from itertools import permutations
from time import perf_counter
from random import randint
from math import exp

alphabet = string.ascii_lowercase
n = 6
variables = tuple(alphabet[:n])

expressions = []
with open('expanded_expressions.txt','r') as f:
    for line in f:
        expressions.append(line.strip())
print(f"{len(expressions)} expressions loaded")

funcs = tuple(eval(f"lambda {','.join(variables)}: {expression}") for expression in expressions)

def insert_values(expression, numbers):
    new_expression = expression
    for char, num in zip(variables, numbers):
        new_expression = new_expression.replace(char, str(num))
    return new_expression

best_metric = 0
# 1.5933155380014143 (28, 74, 6, 73, 1, 47) 984

i = 0
while True:
    numbers = tuple(randint(1,100) for _ in range(n))
    target = randint(200,1000)

    errors = []
    exact_solution = False

    for (f, expr) in zip(funcs, expressions):
        try:
            val = f(*numbers)
        except ZeroDivisionError:
            continue
        error = abs(val - target)
        errors.append(error)
        if error == 0.0:
            exact_solution = True

    errors.sort()

    metric = sum(x * exp(-i / 2) for i,x in enumerate(errors))
    if exact_solution and metric > best_metric:
        best_metric = metric
        print(i, metric, numbers, target, exact_solution, errors[:10])
    i += 1