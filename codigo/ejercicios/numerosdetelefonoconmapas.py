"""
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

"""


n = int(input("Ingresar cantidad de personas..."))
my_dict={}

for x in range(n):
    registro = input().split() #list
    nombre = registro[0]
    numero = int(registro[1])
    my_dict[nombre]=numero

print(type(registro))
print(type(my_dict)) #dict

while True:
    query=input()
    if query in my_dict:
         print(f"{query}={my_dict[query]}")
    else:
        print("Not found")


