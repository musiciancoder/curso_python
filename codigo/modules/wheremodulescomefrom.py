#para ver de donde vienen los modulos q estamos importando

import sys 
print("\n".join(sys.path)) #esto entrega el path de lo que vendria siendo donde esta instalado python en muestro PC. El join() es para  hacerlo mas legible en el output 
print()
print("\n".join(dir())) #muestra todos los metodos y atributos  que tenemos disponibles sin importar nada
print()
print("\n".join(dir(sys))) #muestra todos los metodos y atributos  que tenemos disponible al importar  sys
print()

import stuff.greetings  as gr

print("Greetings: ",gr.__file__) #solo funciona con modulos creados por nosotros