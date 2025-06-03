numbers1 = {2,4,6,7,8,9}
numbers2 = {2,4,6,1,3,5}

print(numbers1.union(numbers2)) # la adicion de elementos de ambos sets
print(numbers1.intersection(numbers2)) # los elementos q estan en la interseccion

print(numbers1.difference(numbers2)) #elementos solo presentes en numbers1
print(numbers1-(numbers2)) #lo mismo de la linea anterior
print(numbers2.difference(numbers1)) #elementos solo presentes en numbers2
print(numbers1.symmetric_difference(numbers2)) # los elementos q no estan en la interseccion
print({1,2,3,4}.issuperset({1,2,3}))#retorna un booleano