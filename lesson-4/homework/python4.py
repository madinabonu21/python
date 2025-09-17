# Python Dictionary and Set Exercises
# Dictionary Exercises
# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

from operator import itemgetter

dict3={1:'Alice',3:'Lalisa',4:'Steven', 2:'Jennie'}

asc=dict(sorted(dict3.items(),key=itemgetter(0)))
desc=dict(sorted(dict3.items(),key=itemgetter(0),reverse=True))

print(asc)
print(desc)

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
# Sample Dictionary:

my_dict={0: 10, 1: 20}

# Expected Result:
# {0: 10, 1: 20, 2: 30}

my_dict[2]=30

print(my_dict)



# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# Expected Result:
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Dictionary (n = 5):
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
squares = {}

for x in range(1, n+1):
    squares[x] = x * x

print(squares)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

# Expected Output:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
n = 1
squared = {}

for x in range(1, 16):
    squared[x] = x * x

print(squared)


# Set Exercises
# 1. Create a Set
# Write a Python program to create a set.

my_set= {1,4,6,}

print (my_set)

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

set1={2,4,5,7,9,13}

for item in set1:
    print(item)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

set2= {3,4,6,12,67,90}
set2.update([4,5])
print (set2)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

set3={1,23,45,60,77}

set3.remove(45)
print(set3)
