#W3SCHOOLS

import numpy as np

#Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

print()

#Iterate on the elements of the following 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr: #If we iterate on a n-D array it will go through n-1th dimension one by one.
  print(x)

print()

#To return the actual values, the scalars, we have to iterate the arrays in each dimension.

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x: 
    print(y)

print()

#Iteracion en arrays 3D

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y: #pero esto causa un problema de q si tenemos n dimensiones necesitamos n bucles for. Para solucionar esto...
      print(z)

print()

#The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

#entregar escalares con los indices(=posiciones en el array)
arr = np.array([[[10, 20, 30, 40], [50, 60, 70, 80]],[[11, 21, 31, 41], [51, 61, 71, 81]]])

for lala, x in np.ndenumerate(arr):
  print(lala, x)