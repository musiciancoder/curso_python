with open("test.txt") as file: #esto es  similar a un try with resources en java. recordar q  un try with resources en java elimina la necesidad de usar finally para cerrar un archivo, por ejemplo
    lines = file.readlines()
    print(lines)