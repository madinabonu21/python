
# 1. Modify String with Underscores
used_chars = ['a', 'e', 'i', 'u', 'o']
index = 2
my_txt = 'abcabcabcdeabcdefabcdefgyy'

while index < len(my_txt) - 1:
    if my_txt[index] not in used_chars:
        used_chars.append(my_txt[index])
        my_txt = my_txt[:index + 1] + '_' + my_txt[index +1:]
        index += 4
        
    else:
        index += 1

print(my_txt)
print(used_chars)

# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
# Example Input:  5
# Example Output:
# 0
# 1
# 4
# 9
# 16

n= int(input("write number : "))

if n < 0: 
        print("number is negative ")
else:
    for i in range(n):
        print(i**2)

# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop

num= 0 

while num < 11:
    print(num)
    num += 1 

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5 

for i in range(1, n+1):
    for j in range(1, i+1 ):
        print(j, end = " ")
    print()



# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Example:
# Enter number 10
# Sum is: 55

num1=10
total= 0

for sum in range(1, num1 + 1):
    total += sum 
print('Total : ', total)

# Exercise 4: Print multiplication table of a given number
# Example:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

n1= 2

for i in range(1, 11):
    print(i * n1 ) # таблица умножения 


# Exercise 5: Display numbers from a list using a loop
# Given:numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected Output:
# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        continue
    if i == 50:      # исключаем именно 50
        continue
    if i == 180:     # исключаем именно 180
        continue
    if i % 5 == 0 :
        print(i)



# Exercise 6: Count the total number of digits in a number
# Example:

# 75869
# Output: 5
nums= 75869
count= 0 

for i in str(nums):
    count += 1 
print(count)

# Exercise 7: Print reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

n2= 5

for i in range(n2, 0, -1):
    for j in range(i, 0 , -1):
        print(j, end = " ")
    print()

# Exercise 8: Print list in reverse order using a loop
# Given: list1 = [10, 20, 30, 40, 50]
# Expected Output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)
    

# Exercise 9: Display numbers from -10 to -1 using a for loop
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution
# Example:

# 0
# 1
# 2
# 3
# 4
# Done!

for i in range(5):
    print(i)
    continue
print("Done!")


# Exercise 11: Print all prime numbers within a range
# Example:
# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47

start= 25
end= 50

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("prime numbers are : ", num)



# Exercise 12: Display Fibonacci series up to 10 terms
# Example:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
n = int(input(' write a number  '))
cnt= 0 
a,b= 0,1

while cnt < n:
    if cnt == 0:
        print(a)
    elif cnt == 1:
        print(b)
    else:
       c= a+b 
       print(c)
       a,b= b,c
    cnt += 1



# Exercise 13: Find the factorial of a given number
# Example:

# 5! = 120
factorial= 1
my_num= int(input("write number :  "))

for i in range(1, my_num+1):
    factorial *= i
print(f"factorial of {my_num} is {factorial}")


# return uncommon elements of lists
# input : 
list1=[1,1,2]
list2=[2,3,4]
# output: [1,1,3,4]

uncommon1= [x for x in list1 if x not in list2]+[y for y in list2 if y not in list1]
print(uncommon1)

# input:
list4=[4,5,6]
list3=[1,2,3]

# output: [1,2,3,4,5,6]

unit_list=list3+ list4
print(unit_list)
#alternative : print(list4+list3)


# input : 
list5=[1,1,2,3,4,2]
list6=[1,3,4,5]
# output: [2,2,5]

result=[x for x in list5 if x not in list6]+[y for y in list6 if y not in list5]

print(result)
