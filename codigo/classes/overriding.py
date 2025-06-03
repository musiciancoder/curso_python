class Animal:
    def speak(self):
        print("Im an animal")

class Cat(Animal):
    def speak(self): #en python no hay sobrecarga de metodos, cada metodo debe llamarse distinto, excepto cuando estamos sobrescribiendo  un metodo como en este caso.
        print("Im an cat")

cat = Cat()
cat.speak()