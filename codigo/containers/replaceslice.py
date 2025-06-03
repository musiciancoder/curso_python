numbers = list((0,1,2,3,4,5,6,7))

numbers[2:4] = (0,0,0,0) #reemplazar de posicion 2 al 4
print(numbers)

numbers[2:6] = [] 
print(numbers)

numbers[1::2] = ["hello","to","you"] #a partir de la posicion 1, de 2 en 2
print(numbers)




