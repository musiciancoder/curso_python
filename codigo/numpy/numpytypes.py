#https://www.w3schools.com/python/numpy/numpy_data_types.asp

import numpy as np

arr = np.array([1, 2, 3, 4])

print(type(arr))  #veremos el tipo que en este caso es array

print(arr.dtype) #veremos el tipo de los elemes del array

arr = np.array([10, 20, 30, 40], dtype='S') #aca definimos eel  tipo como string

print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i') #convertimos a integer un array preexistente con float

print(newarr)
print(newarr.dtype)