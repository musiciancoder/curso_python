fruits1 = "apple","orange"
fruits2 ="banana","grapes"

print(fruits1 + fruits2)
print(fruits1 * 3)
print()

print(id(fruits1)) #cada objeto en python tiene un id que es unico e irrepetiple
fruits1 += fruits2 #aca se crea un nuevo objeto fruits1
print(fruits1)
print(id(fruits1)) #se aprecia que es otro objeto pq tiene id distinto 