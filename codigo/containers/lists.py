#las listas son iguales a los tulips excepto q las listas son modificables y los tulips no. Son como las listas en java.
fruits = ["apple","orange","grape"]

fruits_copy = fruits.copy() #crea un shallow copy
print("fruits_copy ANTES de cambio en fruits: " + str(fruits_copy)) #['apple', 'orange', 'grape']

print(id(fruits))
fruits +=["melon"]
print(id(fruits)) #como tienen el mismo id significa q es el mismo objeto q ha sido modificado

print("fruits_copy DESPUES de cambio en fruits: " + str(fruits_copy)) #['apple', 'orange', 'grape']

print(fruits)

fruits[0] = "strawberry"
print(fruits)

fruits.append("pear") #agrega item al final
print(fruits)

fruits.extend(["blueberry"]) #agrega otra lista (como el addAll de java) 
print(fruits)

fruits.insert(2, "kiwi") #como el set de java
print(fruits)

fruits_tuple = tuple(fruits) #lo pasa a un tuple
print(fruits_tuple)

fruits_list = list(fruits_tuple) #pasa un tuple a lista 
print(fruits_list)