# Homework: List and Tuple Exercises
# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

fruits=['peach','pear','banana','orange','apple']
print(fruits[2])

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

a=[1,3,4]
b=[2,6,9]
b.extend(a)

print(b)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

my_list=[1,4,6,12,56,0,23]

mid_position= len(my_list)//2

middle=my_list[mid_position] if len(my_list)% 2 != 0 else my_list[mid_position-1]

result=[my_list[0],middle,my_list[-1]]

print(result)


# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

movies=['Alice in a wonderland','Awake','Wicked','the princes diaries','Legally Blonde','Enchanted']

mov_name=tuple(movies)

print(mov_name)


# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

cities=['Tokyo','Manchester','Colorado','London','New York','Ibiza']

if "Paris" in cities:
    print('paris in the list')
else :
    print("paris is not in the list")


# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

num=[1,4,5,8,12,4,8]

duplicate=num+num
print(duplicate)


# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

element=[2,3,6,9,40]

element[0],element[-1]=element[-1],element[0]

print(element)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

my_tuple=(1,2,3,4,5,6,7,8,9,10)

print(my_tuple[2:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

colors=['red','blue','pink','blue','yellow','white']

print(colors.count('blue'))

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals=('bear','horse','lion','zebra','turtle')

print(animals.index('lion'))

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

tp1=(1,3,7,8)
tp2=(5,9,2,6)

merged=tp1+tp2

print(merged)


# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

tpl=(3,5,67,78)
lst=[1,7,90,5,3,8]

print(len(tpl))
print(len(lst))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

tuples=(2,4,5)

print(list(tuples))

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

tup1=(3,4,5)

max=max(tup1)
min=min(tup1)

print("max value:", max)
print("min value:", min)


# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

tplwords=('Lisa','Jennie','Jisoo','Rose')
print(tuple(reversed(tplwords)))
