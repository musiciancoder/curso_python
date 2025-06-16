import numpy as np

arr = np.array([1,2,3,4,5])

new_arr = arr > 3 #condicion

print(f"(type new_arr:  {type(new_arr)}")

print(new_arr) #[False False False  True  True]

my_new_arr = arr[new_arr]

print(f"(type my_new_arr:  {type(new_arr)}")

print(my_new_arr)
