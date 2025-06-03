# and, not, or (no existen &&,||  etc).

raining = False
temperature = 20

if temperature > 19 and not raining:
    print("Weather fine")
elif not raining:
     print("At least it's dry")
else:
     print("Stay indoors")

mood = "good" if not raining else "bad" #equivanete a operador ternario de java
print(mood)