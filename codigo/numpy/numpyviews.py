#we can manipulate numpy arrays with views

import numpy as np

values = np.arange(16).reshape(4,4) *10
print(type(values))
print(values)

print()

view = values[:,1:3] #columnas 1 y 2 de values para trabajar con ellas

print()
print(type(view))
print(view)

view *=0 #multiplicar por cero las  columnas 1 y 2

print()

print(view)

print()

print(values) #values ha sifo modificado
