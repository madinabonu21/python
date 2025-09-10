"""QUESTION 1 
Given a side of square. Find its perimeter and area."""

a=int(input('a:'))

# square is a geometric shape with four equal sides and four 90-degree angles 

perimeter= 4*a
area= a**2

print('Perimeter:',perimeter)
print('Area:',area)


''' QUESTION 2 
Given diameter of circle. Find its length.'''

pi= 3.14159
diameter = float(input('diameter:'))

#To find the "length" of a circle, which is its circumference, use the formula C = πd (where d is the diameter).

C= pi*diameter

print('length:',C)


""" QUESTION 3
Given two numbers a and b. Find their mean.
"""

a=int(input('a:'))
b=int(input('b:'))

mean= (a+b)/2

print('mean:',mean)



""" QUEASTION 4 

Given two numbers a and b. Find their sum, product and square of each number.
"""

a= int(input('a:'))
b= int(input('b:'))

sum= a+b
product=a*b
square_a= (pow(a,2))
square_b= (pow(b,2))

print('sum:',sum)
print('product:',product)
print('square_a:',square_a)
print('square_b:',square_b)
