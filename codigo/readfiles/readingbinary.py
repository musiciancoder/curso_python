with open('test.bin','rb') as file:
    data = file.read(5)
    print(type(data))
    print(data)