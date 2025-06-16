with open("test.txt") as file: #esto es  similar a un try with resources en java. recordar q  un try with resources en java elimina la necesidad de usar finally para cerrar un archivo, por ejemplo
    lines = file.readlines()
    print(lines)

"""
W3SCHOOLS
If you are not using the with statement, you must write a close statement in order to close the file:
Example
Close the file when you are finished with it:
f = open("demofile.txt")
print(f.readline())
f.close()
"""