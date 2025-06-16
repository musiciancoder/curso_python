"""
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
The NumPy Random module provides two methods for this: shuffle() and permutation().
"""

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5]) #he shuffle() method makes changes to the original array.

random.shuffle(arr)

print(arr)

print("-----------------------------")



arr = np.array([1, 2, 3, 4, 5])

arr2 = random.permutation(arr) #The permutation() method returns a re-arranged array (and leaves the original array un-changed).

print(arr)
print(arr2)
