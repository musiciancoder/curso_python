from collections import defaultdict

people = {
    "Bob":42,
    "Sue":53,
    "Steve":25,
}

print(people.get("Ethel",99))  #QUE DEVUELVA 99 EN CASO Q ETHEL NO EXISTA EN PEOPLE

days= defaultdict(str) #str es palabra reservada para strings

days.update({"Mon":"monday","Tue":"tuesday"})

print(days)
print(days["Mon"])
print(days["Wed"]) #devuelve un empty string que es el valor por defecto que da defaultdict para un string str