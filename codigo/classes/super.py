class  Machine:
    def __init__(self):
       print("Machine constructor")

class Car(Machine):
    def __init__(self):
        super().__init__ #si bien en python los constructores se heredan,  al igual q java podemos invocar el constructor de la superclase en cualquier metodo por medio de super.
        print("Car constructor")

c=Car() #al crearse un objeto se ejecuta el constructor al igual q en java

print()

#Con atributos (esto lo hice yo, no salia en el  curso)
class Fender:
    def __init__(self, color, price):
        self.color = color
        self.price = price

guitarraFender = Fender("red",1500)
print(guitarraFender.color, guitarraFender.price)

class Stratocaster(Fender):
    pass

guitarraStratocaster = Stratocaster("blue",2000)
print(guitarraStratocaster.color, guitarraStratocaster.price)

class Telecaster(Fender):
     
     def __init__(self, color, price,bridge):    #notar q solo va self en el  constructor de la clase, pero no cuando llamamos a super
      super().__init__(color, price)
      self.bridge = bridge

guitarraTele = Telecaster("blue",2000,"fijo")
print(guitarraTele.color, guitarraTele.price,  guitarraTele.bridge)


