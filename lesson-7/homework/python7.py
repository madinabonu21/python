# 1.is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

def is_prime(n):
    n > 0
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                print(f"{n} is not prime numner")
            break
        else:
            print(f"{n} is prime number")

is_prime(4)


# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum(k):
    print(sum(map(int,str(k))))    

digit_sum(23456)   

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def power_of_two(n):
    for k in range(1,n):
        if 2**k <= n:
            print(2**k , end= " ")
        else:
            break

power_of_two(16)
