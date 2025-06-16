#Formar un diccionario a partir de dos tuples

user_input = input("Enter numbers separated by commas (e.g., 1,2,3): ")
print(type(user_input))
my_tuple = tuple(int(x.strip()) for x in user_input.split(","))
print(my_tuple)

print()

my_list = list(my_tuple)
my_list.insert(2,8)
my_list.append(1)
print(my_list)

print()

my_set = set(my_list)
my_set.add(4)
print(my_set) #notar q no los devuelve ordenados

print()


user_input =  input("Enter strings: ")

my_set_two = set(str(x.strip()) for x in user_input.split(",")) #notar q no los devuelve ordenados, para ello habria q pasarlo a lista y ocupar el metodo sorted ()

sorted(my_set_two)

print(my_set_two)


#Forma 1
#my_dicc=dict(zip(my_set,my_set_two))

#Forma 2. Hay q pasar a list primero pq los sets en python (y en java) no son colecciones que respetan un orden
my_dicc = {}
my_set_list = list(my_set)
my_set_two_list = list(my_set_two)
length = min(len(my_set_list), len(my_set_two_list))

for i in range(length):
    my_dicc[my_set_list[i]] = my_set_two_list[i]

print(my_dicc)

my_dicc_2 = {}

my_dicc_2["guitarra"] = "fender"
my_dicc_2["bajo"] = "gibson"

print(my_dicc_2)
    

