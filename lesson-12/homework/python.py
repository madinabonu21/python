import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_range(start, end, result):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))
num_threads = int(input("Enter number of threads: "))

result = []
threads = []
step = (end_range - start_range + 1) // num_threads

for i in range(num_threads):
    s = start_range + i * step
    e = start_range + (i + 1) * step - 1
    if i == num_threads - 1:
        e = end_range
    t = threading.Thread(target=check_range, args=(s, e, result))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

result.sort()
print("Prime numbers:", result)





# task 2 


import threading
from collections import Counter

def count_words(lines, result):
    words = []
    for line in lines:
        words.extend(line.strip().split())
    result.append(Counter(words))

file_path = input("Enter file path: ")

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

num_threads = int(input("Enter number of threads: "))
total_lines = len(lines)
step = total_lines // num_threads

threads = []
results = []

for i in range(num_threads):
    start = i * step
    end = (i + 1) * step if i != num_threads - 1 else total_lines
    t = threading.Thread(target=count_words, args=(lines[start:end], results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total_count = Counter()
for c in results:
    total_count.update(c)

print("\n=== Word Occurrences ===")
for word, count in total_count.most_common(10):
    print(f"{word}: {count}")
