import math


# Математические операции

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"



# Строковые функции

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


# Геометрия: круг

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


# Операции с файлами

def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()



# Главная программа

def main():
    print("=== Math Operations ===")
    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(3, 7))
    print("Divide:", divide(8, 2))

    print("\n=== String Utils ===")
    print("Reverse:", reverse_string("Python"))
    print("Vowels:", count_vowels("Beautiful Day"))

    print("\n=== Geometry ===")
    print("Area:", calculate_area(5))
    print("Circumference:", calculate_circumference(5))

    print("\n=== File Operations ===")
    file_name = "test.txt"
    write_file(file_name, "Hello, this is a test file.")
    print("File content:", read_file(file_name))


if __name__ == "__main__":
    main()
