def details (name,**kwargs): #string, dict (que es como un mapa)

    print("Name: ", name)

    print()

    print(type(kwargs)) #class 'dict' que es como una especie de hashmap en java

    print()

    if "height" in kwargs: #si existe
        print("Height", kwargs["height"])

    print()

    for key in kwargs:
        print(key, kwargs[key])

details("Sue",height=170,age=42)