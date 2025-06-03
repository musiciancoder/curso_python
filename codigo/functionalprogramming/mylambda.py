# DE W3SCHOOLS !!!
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#Use lambda functions when an anonymous function is required for a short period of time.
#Java doesn't have lambdas exactly like Python's until Java 8, but since Java 8, you can use lambda expressions with functional interfaces, pero
#igual no son exactamente iguales, ya que las Function en java son interfaces funcionales  y en python no señor. 

#sin argumentos
x = lambda a : a + 10
print(x(5))

#con argumentos
x = lambda a, b : a * b
print(x(5, 6))

#muy util para usar dentro de otra funcion
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))