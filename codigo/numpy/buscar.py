import numpy as np
#Find the indexes where the value is 4:

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

"""
The example above will return a tuple: (array([3, 5, 6],)
Which means that the value 4 is present at index 3, 5, and 6.
"""

#Find the indexes where the values are even:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

print("______________")
"""
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
The searchsorted() method is assumed to be used on sorted arrays.
Binary search is an efficient algorithm for finding a target value within a sorted list or array. It works by repeatedly dividing the search interval in half:

Compare the target value to the middle element of the list.
If they are equal, the search is successful.
If the target is less than the middle element, repeat the search on the left half.
If the target is greater, repeat the search on the right half.
Continue until the target is found or the interval is empty.
Time complexity: O(log n)

Note: The list must be sorted for binary search to work.
Example above:
"""
#Find the indexes where the value 7 should be inserted:

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

