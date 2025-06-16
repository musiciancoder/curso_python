"""
Write a Python program that reads an integer from the user and prints the sum of its digits.
Input:
A single integer (can be positive or negative).

Output:
The sum of the digits (ignore the sign).

Example:
"""

myinput = input("Enter an integer: ")

mystring = str(myinput)

mystring = mystring.replace("-", "")  # Remove the negative sign if present 

mylist = mystring.split()  # Split the string into a list of characters

counter = 0
for i in range(len(mylist)):
    counter += int(mylist[i])  # Convert each character back to an integer and add to the counter

print("The sum of the digits is:", counter)

"""
input_number =  abs(int(myinput))

input_number_str = str(input_number)

mylist = input_number_str.split()

print(mylist)

input_number_list = list(input_number_str)

print(input_number_list)

"""







