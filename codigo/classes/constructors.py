class Person: 
    #self es equivalente a this en java, notar q a diferencia de java debemos pasarlo  como argumento en las  funciones (no tiene q llamarse self necesariamente pero es convencion, aunq si debe ser el primer argumento)
    def __init__(self,name): #__ es protected, _es private y sin ni un guion es public. init es una funcion predeterminada para indicar q es constructor 
        self._name = name

    def eating(self):
        print(f"{self._name} is eating") # con f nos separa por espacio automaticamente

    def __str__(self): #equivalente a toString()
        return  f"Hello I am {self._name}"


p= Person("Bob") #creamos un objeto de la clase
p.eating()
print(p)

text = str(p) #otro toString()
print(text)

print(repr(p)) #output __main__.Person object at 0x0000025824836A5
#print(eval(repr(p))) #eval evalue si el  codigo esta bueno o  no 