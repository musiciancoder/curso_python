def calculate_area(width, height, lenght=1): # lenght=1 es valor por defecto; los valores por defecto siempre se pasan al ultimoen los argumentos
    return width * height * lenght


area = calculate_area(2,length=6,height=8 ) #primer argumento ordenado por posicion y segundo y tercer argumento por nombre (no por posicion)

print(area)