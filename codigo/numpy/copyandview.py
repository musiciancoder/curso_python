import numpy as np

"""
https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
"""

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(f"arr:  {arr}")
print(f"copia:  {x}")
print(f"vista:  {y}")

arr[0] = 42

print(f"arr despues:  {arr}")
print(f"copia despues:  {x}") #[1, 2, 3, 4, 5]
print(f"vista despues:  {y}")

"""
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object.
"""

print(x.base)
print(y.base)