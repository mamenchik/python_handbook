#===============A===============
name = input()
mood = input()
print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if mood == "хорошо":
    print("Я за вас рада!")
elif mood == "плохо":
    print("Всё наладится!")

#===============B===============
n1 = int(input())
n2 = int(input())
if n1 > n2:
    print("Петя")
else:
    print("Вася")

#===============C===============
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2:
    if n1 > n3:
        print("Петя")
if n2 > n3:
    if n2 > n1:
        print("Вася")
if n3 > n1:
    if n3 > n2:
        print("Толя")

#===============D===============
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2 > n3:
    print("1. Петя")
    print("2. Вася")
    print("3. Толя")
if n1 > n3 > n2:
    print("1. Петя")
    print("2. Толя")
    print("3. Вася")
if n2 > n1 > n3:
    print("1. Вася")
    print("2. Петя")
    print("3. Толя")
if n2 > n3 > n1:
    print("1. Вася")
    print("2. Толя")
    print("3. Петя")
if n3 > n2 > n1:
    print("1. Толя")
    print("2. Вася")
    print("3. Петя")
if n3 > n1 > n2:
    print("1. Толя")
    print("2. Петя")
    print("3. Вася")

#===============E===============
n = int(input())
m = int(input())
if n > m + 6:
    print("Петя")
else:
    print("Вася")
#===============F===============
year = int(input())
if year % 4 != 0:
    print('NO')
elif year % 100 == 0:
    if year % 400 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('YES')

#===============G===============
number = int(input())
n4 = number % 10
n3 = number // 10 % 10
n2 = number // 100 % 10
n1 = number // 1000
if n1 == n4:
    if n2 == n3:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
#===============H===============
nature = input()

if 'зайка' in nature:
    print('YES')
else:
    print('NO')

#===============I===============
name1 = input()
name2 = input()
name3 = input()
print(min(name1, name2, name3))

#===============J===============
number = int(input())
units = number % 10
dec = number // 10 % 10
hundreds = number // 100
n1 = units + dec
n2 = hundreds + dec
if n1 > n2:
    print(f"{n1}{n2}")
else:
    print(f"{n2}{n1}")

#===============K===============
number = int(input())
n3 = number % 10
n2 = number // 10 % 10
n1 = number // 100
n3_max = 0
n2_max = 0
n1_max = 0
n3_min = 0
n2_min = 0
n1_min = 0
n1_sredn = 0
n2_sredn = 0
n3_sredn = 0
suma = max(n1, n2, n3) + min(n1, n2, n3)
if n3 == max(n1, n2, n3):
    n3_max = 1
elif n2 == max(n1, n2, n3):
    n2_max = 1
elif n1 == max(n1, n2, n3):
    n1_max = 1
if n3 == min(n1, n2, n3):
    n3_min = 1
elif n2 == min(n1, n2, n3):
    n2_min = 1
elif n1 == min(n1, n2, n3):
    n1_min = 1
if (n3_max or n3_min) and (n2_max or n2_min):
    n1_sredn = 1
elif (n2_max or n2_min) and (n1_max or n1_min):
    n3_sredn = 1
elif (n1_max or n1_min) and (n3_max or n3_min):
    n2_sredn = 1
if n1_sredn:
    if suma == n1 * 2:
        print("YES")
    else:
        print("NO")
elif n2_sredn:
    if suma == n2 * 2:
        print("YES")
    else:
        print("NO")
elif n3_sredn:
    if suma == n3 * 2:
        print("YES")
    else:
        print("NO")

#===============L===============
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 >= n2 + n3:
    print("NO")
elif n2 >= n1 + n3:
    print("NO")
elif n3 >= n1 + n2:
    print("NO")
else:
    print("YES")

#===============M===============
n1 = int(input())
n1_1 = n1 // 10
n1_2 = n1 % 10
n2 = int(input())
n2_1 = n2 // 10
n2_2 = n2 % 10
n3 = int(input())
n3_1 = n3 // 10
n3_2 = n3 % 10
if n1_1 == n2_1 == n3_1:
    print(n1_1)
elif n1_2 == n2_2 == n3_2:
    print(n1_2)

#===============N===============
number = int(input())
n3 = number % 10
n2 = number // 10 % 10
n1 = number // 100
n3_max = 0
n2_max = 0
n1_max = 0
n3_min = 0
n2_min = 0
n1_min = 0
n1_sredn = 0
n2_sredn = 0
n3_sredn = 0
suma = max(n1, n2, n3) + min(n1, n2, n3)
if n3 == max(n1, n2, n3):
    n3_max = 1
elif n2 == max(n1, n2, n3):
    n2_max = 1
elif n1 == max(n1, n2, n3):
    n1_max = 1
if n3 == min(n1, n2, n3):
    n3_min = 1
elif n2 == min(n1, n2, n3):
    n2_min = 1
elif n1 == min(n1, n2, n3):
    n1_min = 1
if (n3_max or n3_min) and (n2_max or n2_min):
    n1_sredn = 1
elif (n2_max or n2_min) and (n1_max or n1_min):
    n3_sredn = 1
elif (n1_max or n1_min) and (n3_max or n3_min):
    n2_sredn = 1
# ------------------------1------------------------
if n1_max and n2_sredn and n3_min:
    if n3 == 0:
        print(str(n2), str(n3), " ", str(n1), str(n2), sep="")
    else:
        print(str(n3), str(n2), " ", str(n1), str(n2), sep="")
# ------------------------2------------------------
if n1_min and n2_sredn and n3_max:
    print(str(n1), str(n2), " ", str(n3), str(n2), sep="")
# ------------------------3------------------------
if n2_max and n1_sredn and n3_min:
    if n3 == 0:
        print(str(n1), str(n3), " ", str(n2), str(n1), sep="")
    else:
        print(str(n3), str(n1), " ", str(n2), str(n1), sep="")
# ------------------------4------------------------
if n2_min and n1_sredn and n3_max:
    if n2 == 0:
        print(str(n1), str(n2), " ", str(n3), str(n1), sep="")
    else:
        print(str(n2), str(n1), " ", str(n3), str(n1), sep="")
# ------------------------5------------------------
if n1_max and n3_sredn and n2_min:
    if n2 == 0:
        print(str(n3), str(n2), " ", str(n1), str(n3), sep="")
    else:
        print(str(n2), str(n3), " ", str(n1), str(n3), sep="")
# ------------------------6------------------------
if n1_min and n3_sredn and n2_max:
    print(str(n1), str(n3), " ", str(n2), str(n3), sep="")
#===============O===============
n1 = int(input())
n1_2 = n1 % 10
n1_1 = n1 // 10
n2 = int(input())
n2_2 = n2 % 10
n2_1 = n2 // 10
sredn = n1_1 + n1_2 + n2_1 + n2_2 - max(n1_1, n1_2, n2_1, n2_2) - min(n1_1, n1_2, n2_1, n2_2)
print(max(n1_1, n1_2, n2_1, n2_2), sredn % 10, min(n1_1, n1_2, n2_1, n2_2), sep="")

#===============P===============
v1 = int(input())
v2 = int(input())
v3 = int(input())
if v1 > v2 > v3:
    print(f"{'Петя': ^24}")
    print(f"{'  Вася  ': <24}")
    print(f"{'  Толя  ': >24}")
    print(f"{'   II': <8}{' I ': ^8}{'III   ': >8}")
if v1 > v3 > v2:
    print(f"{'Петя': ^24}")
    print(f"{'  Толя  ': <24}")
    print(f"{'  Вася  ': >24}")
    print(f"{'   II': <8}{' I ': ^8}{'III   ': >8}")
if v2 > v1 > v3:
    print(f"{'Вася': ^24}")
    print(f"{'  Петя  ': <24}")
    print(f"{'  Толя  ': >24}")
    print(f"{'   II': <8}{' I ': ^8}{'III   ': >8}")
if v2 > v3 > v1:
    print(f"{'Вася': ^24}")
    print(f"{'  Толя': <24}")
    print(f"{'  Петя  ': >24}")
    print(f"{'   II': <8}{' I ': ^8}{'III   ': >8}")
if v3 > v1 > v2:
    print(f"{'Толя': ^24}")
    print(f"{'  Петя': <24}")
    print(f"{'Вася  ': >24}")
    print(f"{'   II': <8}{' I ': ^8}{'III   ': >8}")
if v3 > v2 > v1:
    print(f"{'Толя': ^24}")
    print(f"{'  Вася': <24}")
    print(f"{'Петя  ': >24}")
    print(f"{'   II': <8}{' I ': ^8}{'III   ': >8}")

#===============Q===============
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print("No solution")
elif d == 0:
    if (a == b == c == 0):
        print("Infinite solutions")
    elif (a == b == 0):
        print("No solution")
    else:
        x = -b / (2 * a)
        print(f"{x:.2f}")
else:
    if (a == c == 0):
        print(f"{0:.2f}")
    elif a == 0:
        x = -c / b
        print(f"{x:.2f}")
    else:
        x1 = (-b - d ** (0.5)) / (2 * a)
        x2 = (-b + d ** (0.5)) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")

#===============R===============
a = int(input())
b = int(input())
c = int(input())
a_sredn = 0
b_sredn = 0
c_sredn = 0
if (max(a, b, c) == a or min(a, b, c) == a) and (max(a, b, c) == b or min(a, b, c) == b):
    c_sredn = 1
elif (max(a, b, c) == b or min(a, b, c) == b) and (max(a, b, c) == c or min(a, b, c) == c):
    a_sredn = 1
elif (max(a, b, c) == a or min(a, b, c) == a) and (max(a, b, c) == c or min(a, b, c) == c):
    b_sredn = 1
if a_sredn:
    if max(a, b, c) ** 2 == min(a, b, c) ** 2 + a ** 2:
        print("100%")
    elif max(a, b, c) ** 2 < min(a, b, c) ** 2 + a ** 2:
        print("крайне мала")
    elif max(a, b, c) ** 2 > min(a, b, c) ** 2 + a ** 2:
        print("велика")
elif b_sredn:
    if max(a, b, c) ** 2 == min(a, b, c) ** 2 + b ** 2:
        print("100%")
    elif max(a, b, c) ** 2 < min(a, b, c) ** 2 + b ** 2:
        print("крайне мала")
    elif max(a, b, c) ** 2 > min(a, b, c) ** 2 + b ** 2:
        print("велика")
elif c_sredn:
    if max(a, b, c) ** 2 == min(a, b, c) ** 2 + c ** 2:
        print("100%")
    elif max(a, b, c) ** 2 < min(a, b, c) ** 2 + c ** 2:
        print("крайне мала")
    elif max(a, b, c) ** 2 > min(a, b, c) ** 2 + c ** 2:
        print("велика")

#===============S===============
# y <= -44/175 * (x + 7)(x - 5) при y < 0
# x**2 + (y - 5)**2 <= 25 при x >= 0 и y >= 0
# y = 5 при x > -4 и y > 0
# y <= -5/3 * (x + 1) при x <= -4 и y > 0
x, y = float(input()), float(input())
if x ** 2 + y ** 2 > 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif y < 0:
    if y >= 0.25 * x ** 2 + 0.5 * x - 8.75:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
else:
    if x >= 0:
        if x ** 2 + y ** 2 <= 25:
            print("Опасность! Покиньте зону как можно скорее!")
        else:
            print("Зона безопасна. Продолжайте работу.")
    else:
        if x > -4:
            if y <= 5:
                print("Опасность! Покиньте зону как можно скорее!")
            else:
                print("Зона безопасна. Продолжайте работу.")
        else:
            if y <= (5 / 3) * (x + 7):
                print("Опасность! Покиньте зону как можно скорее!")
            else:
                print("Зона безопасна. Продолжайте работу.")


#===============T===============
str1, str2, str3 = input(), input(), input()
if "зайка" in str1 and "зайка" in str2 and "зайка" in str3:
    print(min(str1, str2, str3), len(min(str1, str2, str3)))
elif "зайка" in str1 and "зайка" in str2:
    print(min(str1, str2), len(min(str1, str2)))
elif "зайка" in str1 and "зайка" in str3:
    print(min(str1, str3), len(min(str1, str3)))
elif "зайка" in str2 and "зайка" in str3:
    print(min(str2, str3), len(min(str2, str3)))
elif "зайка" in str1:
    print(str1, len(str1))
elif "зайка" in str2:
    print(str2, len(str2))
elif "зайка" in str3:
    print(str3, len(str3))