import numpy as np

#este snipet es para crear arrays con numpy
arr1= np.array((1,2,3),dtype=np.int32)

print(arr1[1])
tuple1 = arr1.shape
#shape retorna si es  uarray 3x4, 5x1, etc.  en el caso de arr1 como es  de  una sola dimension retorna (3,0)
print(arr1.shape) #NumPy arrays have an attribute called shape that returns a tuple  with each index having the number of corresponding elements.
print(arr1.ndim) # de dimension 1
print(arr1.dtype)
print(len(arr1))

print()

arr2 = np.array([[1.0,  2.1], [2.0, 3.1], [4.0,  2.5]],dtype=np.float64)

print(arr2[1])
print(arr2.shape) #NumPy arrays have an attribute called shape that returns a arr with each index having the number of corresponding elements. 3x2 (filasxcolumnas)
print(arr2.ndim) # de dimension 2
print(arr2.dtype)
print(len(arr2))

