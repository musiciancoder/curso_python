#w3schools

import numpy as np

print("---------------ONE-----------------------")
arr = np.array([1, 2, 3, 4, 5, 6])
print(type(arr)) #<class 'numpy.ndarray'>
newarr = np.array_split(arr, 3) #The return value is a list containing three arrays.
print(type(newarr)) #<class 'list'>
#print(newarr.ndim()) #no se puede pq es lista
#print(newarr.shape()) #no se puede pq es lista
print(newarr)
print(newarr[0]) #muestra el primer array de la lista
print(newarr[1]) #muestra el segundo array de la lista
print(newarr[2]) #muestra el tercer array de la lista

print("---------------TWO-----------------------")
#If the array has less elements than required, it will adjust from the end accordingly.
#Split the array in 4 parts:

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

#Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() 
# worked properly but split() would fail.


print("---------------THREE-----------------------")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(type(newarr))

print(newarr[0])
print(newarr[1])
print(newarr[2])

print("---------------FOUR-----------------------")
"""Splitting 2-D Arrays
Use the same syntax when splitting 2-D arrays.
Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
Split the 2-D array into three 2-D arrays.
"""

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

print("---------------FIVE-----------------------")

"""
The example above returns three 2-D arrays.
Let's look at another example, this time each element in the 2-D arrays contains 3 elements.
Example
Split the 2-D array into three 2-D arrays.
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

print("---------------SIX-----------------------")
"""The example above returns three 2-D arrays.
In addition, you can specify which axis you want to do the split around.
The example below also returns three 2-D arrays, but they are split along the column (axis=1).
Example
Split the 2-D array into three 2-D arrays along columns.
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)

print(newarr) 


print("---------------SEVEN-----------------------")
"""An alternate solution is using hsplit() opposite of hstack()
Example
Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
"""


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)