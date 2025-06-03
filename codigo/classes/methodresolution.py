class A:
    def run(self): #dos metodos q se llaman igual
        print("Hello A")

class B:
    def run(self): #dos metodos q se llaman igual
        print("Hello B")

class C(A,B):
    pass

c=C()
c.run() #no sabemos cual metodo va a tomar

print(C.mro()) #mro permite ver el orden de resolucion y asi saber cual metodo va a tomar. En ultima instancia todos los objetos en Python heredan de la superclase object, igual q en java.
print()
