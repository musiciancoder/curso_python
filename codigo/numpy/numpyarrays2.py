# 3 different ways to create a numpy array

import numpy as np

values1 = np.zeros((2,3)) #2 filas, tres columnas
print(values1)
print(values1.shape)
print(values1.ndim) 
print(values1.dtype)
# print(values1.len()) # no funciona

print()

values2 = np.arange(5, 10, 0.5) # paso de 0.5
print(values2)
print(values2.shape)
print(values2.ndim) 
print(values2.dtype)
# print(values2.len()) # no funciona

print()

values3 = np.linspace(3, 6, 4)
print(values3)
print(values3.shape)
print(values3.ndim) 
print(values3.dtype)
# print(values1.len()) # no funciona

print()