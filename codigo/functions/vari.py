def catalogue(name, *args): # * es porque no se sabe el numero de argumentos

    print("Type: ", type(args)) # el tipo es tuple q es un array no modificable
    print()
    print(name) #Trees
    print()
    if len(args)>=1:
        print(args[0]) #oak
    print()
    for value in args:
        print(value) #"oak","ash","linden"

catalogue("Trees","oak","ash","linden") #toma 
catalogue("Blank")

#name es el nombre del array y *args los valores que contiene.