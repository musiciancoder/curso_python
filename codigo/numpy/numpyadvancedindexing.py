#index para obtener por ejemplo pares ordenados

import numpy as np

values = np.arange(16).reshape(4,4) 
print(type(values))
print(values)

print()

myarray = values[:,[0,2]] #crear un array con las columnas 1 y 2 (el dice q es una lista, yo mas bien creo q es  un array)
print(type(myarray))
print(myarray)

print()

print(values[[0, 2, 2, 3],[0, 0, 2, 1]]) #este indexing toma el (0,0), (2,0),(2,2) y (3,1) de values
