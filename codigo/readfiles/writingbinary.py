data1 = b'Hello' #con esto pasamos al tipo byte, q es inmutable
print(data1)
print(type(data1))

data2 = bytearray([0xFF,1,2,3,4]) # con esto pasamos al tipo bytearray, q es mutable en python al igual que un array de bytes en java

with open('test.bin','wb') as file:
    file.write(data1)

"""
Copilot
Your test.bin file contains the text Hello, which is human-readable because it was saved as plain text, not as raw binary data.

If you write a string like "Hello" to a file in text mode ("w"), it will be saved as readable characters.
If you write bytes (like [10, 20, 30, 40, 50]) in binary mode ("wb"), the file will contain non-printable, non-human-readable data (which would look like 0a141e2832 in hexadecimal).
Summary:

"Hello" is readable because it’s just text.
0a141e2832 is what you’d see if you wrote raw bytes.
"""

# Write text (human-readable)
with open("test2.bin", "w") as f:
    f.write("Hello")

# Write binary (not human-readable)
with open("test3.bin", "wb") as f:
    f.write(bytes([10, 20, 30, 40, 50]))

with open("test3.bin", "rb") as f:
    content = f.read()
    print(content.hex()) #0a141e2832