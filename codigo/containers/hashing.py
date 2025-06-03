#es para ver si un objeto puede ser metido o no en un container
#in java we can only use an element on a set or as a key in a map if we can generate a hashcode from it. Same goes for python.

print(hash((1,2,3))) #podemos agregarlo a set o key de un dictionary

print(hash((1,2,[]))) #NO podemos agregarlo a set o key de un dictionary