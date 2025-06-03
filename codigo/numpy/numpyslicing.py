import numpy as np

values = np.arange(0, 16, 1).reshape(4,4) #4 filas 4 columnas
print(values)

print()

print(values[::2]) #una fila por medio

print()

print(values[::2,1:3]) #una fila por medio y columnas uno y dos