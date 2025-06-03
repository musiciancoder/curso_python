#imprimir los numeros q pasan el filtro en vez de booleanos, a diferencia del snippet de numpycomparisonoperators.py

import numpy as np

values = np.arange(16).reshape(4,4) 
print(type(values))
print(values)

print()

print(values[values%5 ==0])

print()

rng = np.random.default_rng()
numbers = rng.standard_normal(50)
print(numbers.mean())

print()

negatives = numbers[numbers<0]
print(negatives.mean()) # devuelve la media de todos los negativos, o sea el promedio