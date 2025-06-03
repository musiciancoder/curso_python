#Tuples are arrays in java

stuff = ("Charles",7,8.2,True,False,"Cats")

print(stuff[2])
# stuff[2] = "Leaf" #no se puede !

name, value1, value2, bool1,bool2, animal = stuff
print(name, value1, value2, bool1,bool2, animal) #Charles 7 8.2 [True, False, 'Cats'], o sea *other es un 

person, number1, number2, *other = stuff # Charles 7 8.2 [True, False, 'Cats'], o sea *tira como lista los elementos restantes del array
print(person,number1,number2, other)


print(type(other))

animals = ("cat",)
print(animals)