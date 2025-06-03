letters = (chr(x) for x  in range(65,91)) #notar q en python no existe la primitiva char, sino una funcion char
#norar q letters es  un generator

#print(list(letters)) #imprime ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for s in letters:
    print(s, end=" ") # imprime A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


def PowersOfTwo():
    for i in range(8):
        yield 2**i

for x in PowersOfTwo():
    print(x)

print(type(PowersOfTwo()))

"""
Generators in Python are special functions that allow you to create iterators in a more memory-efficient way. Unlike regular functions, generators do not store all values in memory at once; instead, they yield items one at a time using the yield keyword.

Key Features of Generators
Uses yield Instead of return

When a generator function encounters yield, it pauses execution and retains its state.

The next time it's called, it resumes from where it left off.

Memory Efficient

Unlike lists, generators don't store all values at once, making them useful for handling large datasets.

Lazy Evaluation

Values are generated on demand, instead of precomputing everything.
"""



