#igual a los sets de java -->only store unique items and dont have a particular order
numbers = {1,3,6,4}
print(numbers)

for x in numbers:
    print(x)

print(3 in numbers) #si existe o no

print()
numbers.add(7)
print(numbers)

print()
numbers.update([9,8])
print(numbers)

print()
numbers.remove(8)
print(numbers)

print()
numbers.discard(3)
print(numbers)

print()
numbers2=set([1,2,3]) #otra forma de crear sets
print(numbers2)

print()
numbers3 = {n for n in range (5,8)} #otra forma de crear sets
print(numbers3)


