data1 = b'Hello' #con esto pasamos al tipo byte, q es inmutable
print(data1)
print(type(data1))

data2 = bytearray([0xFF,1,2,3,4]) # con esto pasamos al tipo bytearray, q es mutable en python al igual que un array de bytes en java
print(type(data2))
