numbers = [0,1,2,3,4,5,6]

numbers.remove(4)
print(numbers)

value = numbers.pop(1) #retorna el  item q estamos eliminando
print(value, numbers)
print(numbers)

del numbers[2]
print(numbers)

numbers.clear()
print(numbers)

