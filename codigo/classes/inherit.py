class Person: 
    #self es equivalente a this en java, notar q a diferencia de java debemos pasarlo  como argumento en las  funciones
    def __init__(self,name): #__ es protected, _es private y sin ni un guion es public. init es una funcion predeterminada para indicar q es constructor 
        self._name = name

    def eating(self):
        print(f"{self._name} is eating") # con f nos separa por espacio automaticamente

    def __str__(self): #equivalente a toString()
        return  f"Hello I am {self._name}"


p= Person("Bob") #creamos un objeto de la clase

class Employee(Person): #hereda de Person
    def go_on_holyday(self): #en python siempre hay q pasarle como minimo self  a los metodos
        print("Im on holyday")


e=Employee("Sue") #a diferencia de Java,  en Python los constructores SI se heredan
e.eating()
e.go_on_holyday()
