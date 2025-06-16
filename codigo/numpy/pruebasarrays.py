import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr = np.insert(arr, 2, 7)  # Inserts 7 at index 2
print(arr)  # Output: [ 1  2  7  3  4  5]
# Delete the element at index 2 (which is 7)
arr = np.delete(arr, 2)
print(arr)  # Output: [1 2 3 4 5]
# Sort the elements
arr = np.sort(arr)
# Sort the elements in descending order
arr = np.sort(arr)[::-1]
print(arr)  # Output: [1 2 3 4 5]
# Swap the first and last elements
arr[0], arr[-1] = arr[-1], arr[0]
print(arr)  # Output: [5 2 3 4 1]
# Rotate the array by 2 (last 2 elements move to the front)
arr = np.concatenate((arr[-2:], arr[:-2]))
print(arr)  # Output: [4 1 5 2 3]


"""
Here are the main differences between a NumPy array (np.array) and a Python list:

Feature	Python List                 NumPy Array (np.array)
Data Types	Can hold mixed types	Must hold a single data type
Performance	Slower              	Much faster for numerical ops
Memory Usage  Less efficient	    More efficient (contiguous memory)
Functionality	Basic operations	Advanced math, broadcasting, etc.
Syntax	Built-in	                Requires import numpy as np
Vectorized Ops	Not supported	    Supported (e.g., arr * 2)
"""


