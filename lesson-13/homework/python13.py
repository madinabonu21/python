# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime, date

birthdate_str = input("Введите дату рождения (гггг-мм-дд): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

today = date.today()

# Вычисляем возраст
years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

# Корректируем, если месяц или день отрицательные
if days < 0:
    months -= 1
    days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

if months < 0:
    years -= 1
    months += 12

print(f"Ваш возраст: {years} лет, {months} месяцев, {days} дней")


# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime, date, timedelta

birthdate_str = input("Введите дату рождения (гггг-мм-дд): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

today = date.today()
next_birthday = date(today.year, birthdate.month, birthdate.day)

# Если день рождения уже прошёл в этом году
if next_birthday < today:
    next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

days_remaining = (next_birthday - today).days
print(f"До вашего следующего дня рождения осталось {days_remaining} дней")

 
# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

current_str = input("Введите текущие дату и время (гггг-мм-дд ЧЧ:ММ): ")
current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")

hours = int(input("Введите длительность встречи (часы): "))
minutes = int(input("Введите длительность встречи (минуты): "))

end_time = current_time + timedelta(hours=hours, minutes=minutes)
print(f"Встреча закончится: {end_time.strftime('%Y-%m-%d %H:%M')}")


# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

datetime_str = input("Введите дату и время (гггг-мм-дд ЧЧ:ММ): ")
current_tz = input("Введите вашу временную зону (например, Europe/Moscow): ")
target_tz = input("Введите целевую временную зону (например, Asia/Tashkent): ")

dt_naive = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

# Добавляем исходную временную зону
current_zone = pytz.timezone(current_tz)
dt_aware = current_zone.localize(dt_naive)

# Конвертируем в целевую зону
target_zone = pytz.timezone(target_tz)
dt_converted = dt_aware.astimezone(target_zone)

print("Дата и время в целевой зоне:", dt_converted.strftime("%Y-%m-%d %H:%M"))

# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime, timedelta
import time

future_str = input("Введите дату и время будущего события (гггг-мм-дд ЧЧ:ММ:СС): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future_time - now
    if remaining.total_seconds() <= 0:
        print("Время наступило!")
        break
    print("Осталось:", remaining)
    time.sleep(1)  # обновление каждую секунду


# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

email = input("Введите email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Email корректный")
else:
    print("Email некорректный")


# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
phone = input("Введите номер телефона (10 цифр): ")

formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print("Отформатированный номер:", formatted)



# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

password = input("Введите пароль: ")

if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password)):
    print("Пароль надёжный")
else:
    print("Пароль слабый")


# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

occurrences = [i for i in range(len(text)) if text.startswith(word, i)]
print(f"Слово '{word}' встречается {len(occurrences)} раз(а) в тексте.")

# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

text = input("Введите текст: ")
# Простейший паттерн для формата гггг-мм-дд
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)

print("Найденные даты:", dates)
