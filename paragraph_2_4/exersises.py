#===============A===============
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ") if j != n else print(i * j)
#===============B===============
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{j} * {i} = {i * j}")
#===============C===============
n = int(input())
size = 1
num = 1
while num <= n or num == 1:
    for i in range(size):
        if num > n:
            break
        else:
            print(num, end=" ")
            num += 1
    print()
    size += 1
#===============D===============
n = int(input())
suma = 0
for _ in range(n):
    string = input()
    for j in string:
        suma = suma + int(j)
print(suma)
#===============E===============
n = int(input())
flag = False
amount = 0
for i in range(n):
    while (string := input()) != "ВСЁ":
        if "зайка" in string or flag:
            flag = True
        else:
            flag = False
    amount = amount + 1 if flag else amount
    flag = False
print(amount)
#===============F===============
n = int(input())
for i in range(n - 1):
    if not i:
        N, M = int(input()), int(input())
    else:
        N = int(input())
    if N < M:
        N, M = M, N
    while N % M != 0:
        N, M = M, N % M
print(M)
#===============G===============
n = int(input())
size = 3
for i in range(n):
    for j in range(size, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i + 1}!!!")
    size += 1
#===============H===============
n = int(input())
suma = 0
max_suma = 0
max_name = ""
for i in range(n):
    name, num = input(), input()
    for char in num:
        suma = suma + int(char)
    if max_suma <= suma:
        max_suma = suma
        max_name = name
    suma = 0
print(max_name)
#===============I===============
n = int(input())
result = ""
for i in range(n):
    num = input()
    max_num = "0"
    for char in num:
        if char > max_num:
            max_num = char
    result += max_num
print(result)
#===============J===============
n = int(input())
print("А Б В")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j < n:
            print(f"{i} {j} {n - i - j}")
        else:
            break
#===============K===============
n = int(input())
amount = 0
for i in range(n):
    num = int(input())
    prime = 1
    if (num == 1):
        prime = 0
    else:
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                prime = 0
    if prime:
        amount += 1
print(amount)
#===============L===============
n, m = int(input()), int(input())
num = 1
size = len(str(n * m))
for i in range(n):
    for j in range(m):
        print(f"{num: >{size}}", end=" ")
        num += 1
    print()
#===============M===============
n, m = int(input()), int(input())
num = 1
size = len(str(n * m))
for i in range(1, n + 1):
    for j in range(m):
        print(f"{i + n * j: >{size}}", end=" ")
    print()
#===============N===============
n, m = int(input()), int(input())
num = 0
size = len(str(n * m))
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            num = i * m + 1 if not j else num + 1
        else:
            num = num + m if not j else num - 1
        print(f"{num: >{size}}", end=" ")
    print()
#===============O===============
n, m = int(input()), int(input())
num = 0
size = len(str(n * m))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j % 2 == 0:
            num = n * j + 1 - i
        else:
            num = n * j - (n - i)
        print(f"{num: >{size}}", end=" ")
    print()
#===============P===============
n, size = int(input()), int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        num = i * j
        print(f"{num: ^{size}}") if j == n else print(f"{num: ^{size}}", end="|")
    if i != n:
        print("-" * (size * n + n - 1))
#===============Q===============
n = int(input())
amount = 0
for i in range(n):
    num = input()
    if num == num[::-1]:
        amount += 1
print(amount)
#===============R===============
n = int(input())
size = 1
max_len = 0
num = 1
while num <= n or num == 1:
    len_size = 0
    for i in range(size):
        if num > n:
            break
        else:
            len_size += len(str(num)) if (i == size - 1) or (num == n) else len(str(num)) + 1
            num += 1
    if max_len < len_size:
        max_len = len_size
    size += 1
num = 1
size = 1
while num <= n or num == 1:
    string = ""
    for i in range(size):
        if num > n:
            break
        else:
            string = string + str(num) + " " if i != size - 1 else string + str(num)
            num += 1
    print(f"{string:^{max_len}}")
    size += 1
#===============S===============
n = int(input())
size = len(str((n + 1) // 2))
for i in range(n):
    for j in range(n):
        print(f"{min(i + 1, j + 1, n - i, n - j):>{size}}", end=" ")
    print()
#===============T===============
n = int(input())
max_sum = 0
max_si = 0
for si in range(2, 11):
    num = n
    num_str = ""
    suma = 0
    while num > 0:
        num_str += str(num % si)
        num //= si
    for char in num_str:
        suma += int(char)
    if max_sum < suma:
        max_sum = suma
        max_si = si
print(max_si)
