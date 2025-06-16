"""
Write a Python program that reads a string from the user and prints the string reversed.

Input:
A single line of text.

Output:
The reversed string.

Example:

Input: hello world  
Output: dlrow olleh
"""

myinput  = input("Write a sentence: ")
lala = str("")
for i in range(len(myinput)-1,-1,-1):
    lala += myinput[i]

print(lala)


