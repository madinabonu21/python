# Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.

import json  # импортируем библиотеку для работы с JSON


# Чтение файла students.json
with open('students.json', 'r') as file:
    students = json.load(file)  # загружаем JSON в переменную students

# Выводим информацию о каждом студенте
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

import json

# Функции для работы с JSON
def load_books():
    with open('books.json', 'r') as file:
        return json.load(file)

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)  # записываем красиво с отступами

def add_book():
    books = load_books()
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = int(input("Введите год: "))
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Книга успешно добавлена!")

def update_book():
    books = load_books()
    title = input("Введите название книги для обновления: ")
    for book in books:
        if book['title'].lower() == title.lower():
            book['author'] = input("Введите нового автора: ")
            book['year'] = int(input("Введите новый год: "))
            save_books(books)
            print("Книга успешно обновлена!")
            return
    print("Книга не найдена.")

def delete_book():
    books = load_books()
    title = input("Введите название книги для удаления: ")
    books = [book for book in books if book['title'].lower() != title.lower()]
    save_books(books)
    print("Книга удалена успешно!")

# Меню для пользователя
while True:
    print("\n1. Добавить книгу\n2. Обновить книгу\n3. Удалить книгу\n4. Выход")
    choice = input("Выберите действие: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        break
    else:
        print("Неверный выбор!")
