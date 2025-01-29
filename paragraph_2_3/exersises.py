#===============A===============
while (word := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")
#===============B===============
amount = 0
while (string := input()) != "Приехали!":
    if "зайка" in string:
        amount = amount + 1
print(amount)
#===============C===============
k, n = int(input()), int(input())
string = ""
for i in range(k, n + 1):
    # почему тернарный аналог выдаёт ошибку компиляции?
    if i != n:
        string = string + str(i) + " "
    else:
        string = string + str(i)
print(string)

#===============D===============
k, n = int(input()), int(input())
string = ""
if k < n:
    for i in range(k, n + 1):
        if i != n:
            string = string + str(i) + " "
        else:
            string = string + str(i)
    print(string)
else:
    for i in range(k, n - 1, -1):
        if i != n:
            string = string + str(i) + " "
        else:
            string = string + str(i)
    print(string)
#===============E===============
total = 0
while (price := input()) != "0":
    # почему тернарный аналог выдаёт ошибку компиляции?
    if float(price) >= 500:
        total = total + 0.9 * float(price)
    else:
        total = total + float(price)
print(total)

#===============F===============
# 1. Большее число делим на меньшее.
# 2. Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
# 3. Если есть остаток, то большее число заменяем на остаток от деления.
# 4. Переходим к пункту 1.
N, M = int(input()), int(input())
if N < M:
    N, M = M, N
while N % M != 0:
    N, M = M, N % M
print(M)
#===============G===============
# НОК = |N * M| / НОД
N, M = int(input()), int(input())
N_orig, M_orig = N, M
if N < M:
    N, M = M, N
while N % M != 0:
    N, M = M, N % M
print(int(abs(N_orig * M_orig) / M))
#===============H===============
string, N = input(), int(input())
for i in range(N):
    print(string)
#===============I===============
N = int(input())
factorial = 1
while N != 0:
    factorial = factorial * N
    N = N - 1
print(factorial)
#===============J===============
x, y = 0, 0
while (direct := input()) != "СТОП":
    dist = int(input())
    match direct:
        case "СЕВЕР":
            y = y + dist
        case "ЮГ":
            y = y - dist
        case "ВОСТОК":
            x = x + dist
        case "ЗАПАД":
            x = x - dist
print(f"{y}\n{x}")

#===============K===============
N = int(input())
suma = 0
for i in range(len(str(N))):
    suma = suma + N % 10
    N = N // 10
print(suma)
#===============L===============
N = int(input())
max_num = 0
for i in range(len(str(N))):
    if max_num < N % 10:
        max_num = N % 10
    N = N // 10
print(max_num)
#===============M===============
amount = int(input())
for i in range(amount):
    if not i:
        string = input()
    else:
        if (name := input()) < string:
            string = name
print(string)
#===============N===============
# Один из способов — перебор делителей от 2 до корня из числа.
# Если число делится на какое-либо из этих чисел без остатка,
# то оно не является простым
n = int(input())
prime = 1
if (n == 1):
    prime = 0
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = 0
        else:
            pass
if (prime):
    print("YES")
else:
    print("NO")
#===============O===============
n = int(input())
amount = 0
for i in range(n):
    if "зайка" in (string := input()):
        amount = amount + 1
print(amount)
#===============P===============
n = input()
pal = 1
if len(n) == 1:
    pal = 0
else:
    for i in range(len(n)):
        if n[i] == n[len(n) - i - 1]:
            pal = 1 if pal else 0
        else:
            pal = 0
if pal:
    print("YES")
else:
    print("NO")

#===============Q===============
n = input()
string = ""
for i in range(len(n)):
    if (int(n[i]) % 2 != 0):
        string = string + n[i]
print(string)
#===============R===============
n = int(input())
string = ""
i = 2
while i <= n ** 0.5:
    while n % i == 0:
        n = n // i
        string = string + f"{i} * "
    i = i + 1
if n > 1:
    string = string + str(n)
else:
    string = string[:-2]
print(string)
#===============S===============
n = 500
maxi = 1000
mini = 1
print(n)
while (string := input()) != "Угадал!":
    match string:
        case "Меньше":
            maxi = n
        case "Больше":
            mini = n
    if mini == 998:
        n = 1000
    elif maxi == 2:
        n = 1
    else:
        n = mini + ((maxi - mini) // 2)
    print(n)
#===============T===============
# h0 = 37 * (m0 + r0) % 256
# b0 = 37 * (m0 + r0) + r0 * 256 + m0 * 256^2
# h1 = 37 * (m1 + r1) % 256
# b1 = 37 * (m1 + r1) + r1 * 256 + m1 * 256^2
# 2 неизвестные одно уравнение, что делать?
N = int(input())