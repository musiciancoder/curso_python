days = {
    "Mon":"Monday",
    "Tue":"Tuesday",
    "Wed":"Wednesday",
    "Thu":"Thursday"
}

del days["Mon"]

print(days)

popi = days.pop("Tue") #retorna el valor borrado
print(popi)

days.clear() #deja el diccionario vacio.
print(days)