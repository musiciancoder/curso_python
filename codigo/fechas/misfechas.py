#De w3schools

import datetime

x = datetime.datetime.now()
print(x)

print()

print(x.year)
print(x.strftime("%A"))

#create objects
x = datetime.datetime(2020, 5, 17)

print()

print(x)

print()



x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) #%B es un formato .  la  lista de todos los formatos legales esta en w3schools