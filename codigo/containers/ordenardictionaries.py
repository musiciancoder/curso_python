my_dict = {}
my_dict[50]="perro"
my_dict[41]="caballo"
my_dict[42]="gato"
print(my_dict)

"""
/*
    Ordered or Unordered?
    As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

    When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

    Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
*/
"""

# my_dict.sort() #there is no sort() method for dictionaries in Python.
#Dictionaries are unordered collections (before Python 3.7) and do not support sorting in place

#Metodo1 dado por chat gtp
for key, value in sorted(my_dict.items(), key=lambda item: item[1]):
    print(key, value)


    



