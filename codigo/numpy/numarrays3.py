# crear arrays random de varias dimensiones

import numpy as np

values1 = np.random.rand(2,3) #2 filas, tres columnas
print(values1)

print()

rng =  np.random.default_rng()
print(rng)
print()

values2 =  rng.standard_normal((4,3))
print(values2)
print()

print(values2.reshape(2,6))
print(values2)


