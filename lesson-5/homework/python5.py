def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2000))

# 2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n=int(input("n= "))

if n%2 !=0:
    print("weird")
elif n%2 == 0 and 2<= n <=5:
    print("Not weird ")
elif n%2 == 0 and 6<= n <= 20:
    print("Weird")
elif n%2 ==0 and n >=20:
    print("Not Weird")

# Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.
# Solution 1 with if-else statement.

a=int(input("a= "))
b=int(input("b= "))

if a%2 ==0:
    start = a
else:
    start= a+1

print(list(range(start,b+1,2)))


# Solution 2 without if-else statement.


a=int(input("a= "))
b=int(input("b= "))

print(list(range(a + a % 2, b + 1, 2)))  #range(start, stop, step)
