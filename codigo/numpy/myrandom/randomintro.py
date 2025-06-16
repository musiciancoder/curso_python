from numpy import random

my_float = random.rand() #con argumento crearia un array

print(my_float)

my_int = random.randint(100)

print(my_int) #debe llevar argumento

x=random.randint(100, size=5)

print(type(x))

print(x)

print("-----------------------------")

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random

x = random.randint(100, size=(3, 5)) #3x5

print(x.dtype)

print(x)

#Float array

x = random.rand(3, 5)

print(x.dtype)

print(x)

print("-----------------------------")

x = random.choice([3, 5, 7, 9]) #elegir uno de los 4

print(x)

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)