#w3schools

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

print("----------------------------")

#Join two 2-D arrays along rows (axis=1)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

print("------------STACK----------------")

"""
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
"""
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1) #1,4 es una fila, 2,5 es una fila, 3,6 es otra fila

print(arr.ndim)
print(arr.shape) #3 filas, 2 columnas
print(arr)

#arr = np.stack((arr1, arr2), axis=0) igual es posible, y daria (2, 3)[[1 2 3] [4 5 6]]

print("----------------------------")


#NumPy provides a helper function: hstack() to stack along rows.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr.shape) #6x0
print(arr)
print("----------------------------")

#NumPy provides a helper function: vstack()  to stack along columns.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr.shape) #2filasx3columnas
print(arr)
print("----------------------------")

#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2)) #(1, 3, 2) -->dimendion 3D
print(arr.ndim)
print(arr.shape)
print(arr)
