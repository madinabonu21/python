# Homework:
# Object-Oriented Programming (OOP) Exercises
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.141
    
    def area(self):
        return self.pi * (self.radius**2)
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * self.pi * self.radius


r = float(input("Enter the radius of the circle: "))
circle = circle(r)

print(f"Area of circle: {circle.area():.2f}")
print(f"Perimeter of circle: {circle.perimeter():.2f}")
    

# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.


from datetime import date , datetime 

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name 
        self.country = country
        self.birth_date = datetime.fromisoformat(birth_date).date()

    def calculate_age(self):
        today=date.today()
        age=today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1
                return age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.birth_date}")
        print(f"Age: {self.calculate_age()} years")


person1= Person("Madina","tashkent","2004-10-21")
person1.display_info()
        
# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def division(self):
        return self.x // self.y
    
    def multiplication(self):
        return self.x * self.y
    
calc=Calculator(10,5)
    
print(f"result of division : {calc.division()}")
print(f"result of Multiplication : {calc.multiplication()}")

# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

class Shape:
    def are(self):
        pass
    def perimeter(self):
        pass

    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.pi = 3.141
        
        def area(self):
            return self.pi * (self.radius ** 2 )
        
        def perimeter(self):
            return self.pi * 2 * self.radius
        
    class Square:
        def __init__(self, side):
            self.side = side 

        def area(self):
            return self.side**2
        
        def perimeter(self):
            return self.side * 4 
        
    class Triangle:
        def __init__(self, a, b, c):
            self.a,self.b,self.c = a,b,c

        def area(self):
            s = (self.a + self.b + self.c)/2
            return (s * (s-self.a)*(s-self.b)* (s-self.c)) * 0.5
        
        def perimeter(self):
            return(self.a + self.b + self.c)    

square = Shape.Square(4)
circle = Shape.Circle(4)
triangle = Shape.Triangle(2,4,5)

print(f"Area of circle is {circle.area()} and perimeter is {circle.perimeter()}")
print(f"Area of square is {square.area()} and perimeter is {square.perimeter()}")
print(f"Area of triangle is {triangle.area()} and perimeter is {triangle.perimeter()}")


# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)


# Test
tree = BinarySearchTree()
for n in [8, 3, 10, 1, 6, 14]:
    tree.insert(n)

print(tree.search(6))   # True
print(tree.search(15))  # False


# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def pop(self):
        if not self.items:
            print("Stack is empty.")
        else:
            print(f"Removed: {self.items.pop()}")

# Test
s = Stack()
s.push(10)
s.push(20)
s.pop()
s.pop()
s.pop()


# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Test
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.delete(20)
ll.display()


# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())

# Test
cart = ShoppingCart()
cart.add_item("Apple", 1.5)
cart.add_item("Banana", 2.0)
print("Total:", cart.total_price())
cart.remove_item("Apple")
print("Total after remove:", cart.total_price())


# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Stack is empty.")
        else:
            self.items.pop()

    def display(self):
        print("Stack:", self.items)

# Test
s = Stack()
s.push(5)
s.push(10)
s.display()
s.pop()
s.display()


# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            print("Queue is empty.")
        else:
            self.items.pop(0)

    def display(self):
        print("Queue:", self.items)

# Test
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()


# 11. Bank Class
# # Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0):
        self.accounts[name] = balance
        print("Account created.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
        else:
            print("Account not found.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def display_accounts(self):
        for name, balance in self.accounts.items():
            print(f"{name}: {balance}")

# Test
bank = Bank()
bank.add_account("Alice", 1000)
bank.deposit("Alice", 500)
bank.withdraw("Alice", 300)
bank.display_accounts()
