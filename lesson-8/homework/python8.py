# Python Exception Handling: Exercises, Solutions, and Practice
# Exception Handling Exercises
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try: 
    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))

    division = num1/num2
    print(division)

except ZeroDivisionError:

    print(" You cannot divide a number by zero!")

else:
    
    print("Division performed successfully.")

finally:
   
    print("Program execution completed.")




# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    value=int(input("write a number: "))

except ValueError:
    print("value is not integer")

else:
    print("value is integer")

finally:
    print("Program execution completed.")

# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    file_name = input("Enter file name: ") 
    with open (file_name, 'r') as file:
        content = file.read()
        print("File content: ")
        print(file)
except FileNotFoundError:
    print("File was not found , please check it and try again ")


# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(f"The sum of {x} and {y} is {x + y}")

except ValueError:
    raise TypeError("Inputs must be numerical!")



# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.


try:
    file_name = input("Enter the file name: ")


    with open(file_name, 'r') as file:
        print("File opened successfully!")
        print(file.read())

except PermissionError:
    print("Error: Permission denied! You don't have access to this file.")

except FileNotFoundError:
    print("Error: File not found. Please check the file name and path.")

finally:
    print("Program execution completed.")


# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    my_list = input("List : ")

except IndexError:
    print("Index error check and try again ")

else:
    print("Given list is correct")

finally:
    print("Program execution completed.")



# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")


# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ArithmeticError:
    print("Arithmetic error occurred (e.g., division by zero).")


# Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open("sample.txt", "r", encoding="ascii") as file:
        print(file.read())
except UnicodeDecodeError:
    print("Encoding error: could not read file properly.")


# Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    my_list = [1, 2, 3]
    my_list.push(4)  # Ошибка! У списка нет метода push
except AttributeError:
    print("AttributeError: List object has no such method.")


# Python File Input Output: Exercises, Practice, Solution
# File Input/Output Exercises
# Write a Python program to read an entire text file.

with open("sample.txt", "r") as file:
    print(file.read())

# Write a Python program to read first n lines of a file.

n = int(input("Enter number of lines to read: "))
with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")


# Write a Python program to append text to a file and display the text.

with open("sample.txt", "a") as file:
    file.write("\nThis is a new line.")
with open("sample.txt", "r") as file:
    print(file.read())


# Write a Python program to read last n lines of a file.

n = int(input("Enter number of last lines: "))
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end="")


# Write a Python program to read a file line by line and store it into a list.

with open("sample.txt", "r") as file:
    lines = file.readlines()
print(lines)


# Write a Python program to read a file line by line and store it into a variable.

text = ""
with open("sample.txt", "r") as file:
    for line in file:
        text += line
print(text)


# Write a Python program to read a file line by line and store it into an array.

with open("sample.txt", "r") as file:
    data = [line.strip() for line in file]
print(data)


# Write a Python program to find the longest words.

with open("sample.txt", "r") as file:
    words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)


# Write a Python program to count the number of lines in a text file.

with open("sample.txt", "r") as file:
    count = len(file.readlines())
print("Number of lines:", count)


# Write a Python program to count the frequency of words in a file.

from collections import Counter
with open("sample.txt", "r") as file:
    words = file.read().split()
freq = Counter(words)
print(freq)


# Write a Python program to get the file size of a plain file.

import os
print("File size:", os.path.getsize("sample.txt"), "bytes")


# Write a Python program to write a list to a file.

data = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as file:
    for item in data:
        file.write(item + "\n")


# Write a Python program to copy the contents of a file to another file.

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())


# Write a Python program to combine each line from the first file with the corresponding line in the second file.

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())


# Write a Python program to read a random line from a file.

import random
with open("sample.txt", "r") as file:
    lines = file.readlines()
print(random.choice(lines))


# Write a Python program to assess if a file is closed or not.

file = open("sample.txt", "r")
print(file.closed)
file.close()
print(file.closed)


# Write a Python program to remove newline characters from a file.

with open("sample.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)


# Write a Python program that takes a text file as input and returns the number of words in a given text file.

with open("sample.txt", "r") as file:
    text = file.read()
words = text.replace(",", " ").split()
print("Number of words:", len(words))


# Note: Some words can be separated by a comma with no space.
# Write a Python program to extract characters from various text files and put them into a list.

files = ["a.txt", "b.txt"]
chars = []
for name in files:
    with open(name, "r") as file:
        chars.extend(list(file.read()))
print(chars)


# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")


# Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string
letters = string.ascii_uppercase
n = int(input("How many letters per line? "))
with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")
