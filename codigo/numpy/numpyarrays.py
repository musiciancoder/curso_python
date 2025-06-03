import numpy as np

#este snipet es para crear arrays con numpy

tuple1 = np.array((1,2,3),dtype=np.int32)

print(tuple1[1])
print(tuple1.shape) #aca se ve q es un tuple
print(tuple1.ndim) # de dimension 1
print(tuple1.dtype)
print(len(tuple1))

print()

tuple2 = np.array([1.0,  2.1], [2.0, 3.1], [4.0,  2.5],dtype=np.float64)

print(tuple2[1])
print(tuple2.shape) #aca se ve q es un tuple
print(tuple2.ndim) # de dimension 3
print(tuple2.dtype)
print(len(tuple2))

