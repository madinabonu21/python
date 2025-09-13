# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
from datetime import date
name=input("Your name : ")
year_of_birth= int(input("Year of birth : "))

current_year= date.today().year

age=current_year-year_of_birth

print(f" hello your name {name} , and you are {age} years old")

# 2. Extract Car Names
# Extract car names from the following text:

txt = 'LMaasleitbtui'

car_1=txt[::2] #получаем буквы в индексах 2,4,6
car_2=txt[1::2] #получаем буквы в индексах 1,3,5

print(car_1)
print(car_2)

# 3. Extract Car Names
# Extract car names from the following text:

txts = 'MsaatmiazD'

cars_1 = txts[::2]
cars_2= txts[1::2]

print(cars_1)

for ch in reversed(cars_2):
    print(ch, end= "")

# 4. Extract Residence Area Extract the residence area from the following text: 
# txt = "I'am John. I am from London"

txt = "I'am John. I am from London"

part=txt.split("from")
residence=part[1].strip()

print(residence)


# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

a=input("write something : ")

print(a[::-1])

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

count=0
word=input("write something : ")
vowels='aioueAEOUI'

for ch in word:
    if ch in vowels:
        count +=1

print ("vowels in this word : ", count)



# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = list(map(int,input("write numbers: ").split())) #map переводит каждое число в int т.к split  разделяет каждое число на отдельный str

maximum = max(numbers)

print ("Max value : ", maximum)

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word=input("write something : ")

if word == word[::-1]:
    print("palindrome")
else :
    print ("not palindrome")



# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email=input("write your email: ")

domain=email.split("@")[1]

print("Domain: ", domain)

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.


import random
import string

# задаем длину пароля
length = 12  

# наборы символов
digits = string.digits                # 0123456789
lowercase = string.ascii_lowercase    # abcdefghijklmnopqrstuvwxyz
uppercase = string.ascii_uppercase    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"

# объединяем всё
chars = digits + lowercase + uppercase + symbols

# собираем пароль
password = "".join(random.choice(chars) for _ in range(length))

print("Случайный пароль:", password)

