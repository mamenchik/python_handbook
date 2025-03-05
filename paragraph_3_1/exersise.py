#===============A===============
flag = 1
for _ in range(int(input())):
    text = input()
    if not (text.startswith("а") or text.startswith("б") or text.startswith("в")):
        flag = 0
        break
print("YES") if flag else print("NO")
#===============B===============
text = input()
for char in text:
    print(char)
#===============C===============
l, n = int(input()), int(input())
for i in range(n):
    text = input()
    if len(text) > l:
        for i in range(l - 3):
            print(f"{text[i]}", end="")
        print("...")
    else:
        print(text)
#===============D===============
while (text := input()) != "":
    if not text.endswith("@@@"):
        if not (text.startswith("##")):
            print(text)
        else:
            print(text[2:])
#===============E===============
text = input()
print("YES") if text == text[::-1] else print("NO")
#===============F===============
amount = 0
for _ in range(int(input())):
    text = input()
    amount += text.count("зайка")
print(amount)
#===============G===============
text = input()
digits = text.split(" ")
print(int(digits[0]) + int(digits[1]))
#===============H===============
for _ in range(int(input())):
    text = input()
    if "зайка" in text:
        print(text.index("зайка") + 1)
    else:
        print("Заек нет =(")
#===============I===============
while (text := input()) != "":
    if "# " in text:
        for i in range(text.find("# ")):
            if i != text.find("# ") - 1:
                print(text[i], end="")
            else:
                print(text[i])
    else:
        print(text)
#===============J===============
all_txt, max_char = "", ""
max_count = 0
while (text := input()) != "ФИНИШ":
    text = text.lower()
    all_txt += text
for char in all_txt:
    if char != " ":
        if all_txt.count(char) > max_count:
            max_count = all_txt.count(char)
            max_char = char
print(max_char)
#===============K===============
all_req = []
for _ in range(int(input())):
    all_req.append(input())
req = input().lower()
for i in all_req:
    if req in i.lower():
        print(i)
#===============L===============
porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(int(input())):
    print(porridges[i % 5])
#===============M===============
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
power = int(input())
for i in numbers:
    print(i ** power)
#===============N===============
digits, power = input(), int(input())
numbers = list(map(int, digits.split()))
result = [x ** power for x in numbers]
print(*result)
#===============O===============
digits = input()
numbers = list(map(int, digits.split()))
M = 0
for i in range(len(numbers) - 1):
    if not i:
        N, M = numbers[i], numbers[i + 1]
    else:
        N = numbers[i + 1]
    while N % M != 0:
        N, M = M, N % M
print(M)
#===============P===============
# WRONG!!!
L = int(input())
headers, text_len = [], 0
header = ""
for i in range(int(input())):
    if len(string := input()) + text_len < L:
        headers.append(string)
        text_len += len(string)
    else:
        for j in range(L - text_len - 3):
            header += string[j] if j < L - text_len - 3 else "..."
        headers.append(header)
        break
print(*headers)
#===============Q===============
string = input()
string = string.lower()
str_mod = ""
for char in string:
    if char != " ":
        str_mod += char
if str_mod == str_mod[::-1]:
    print("YES")
else:
    print("NO")
#===============R===============
numbers, amounts, i = [], [], 0
text = input()
while i < len(text):
    ind = 0
    while i + ind < len(text) and text[i + ind] == text[i]:
        ind += 1
    numbers.append(text[i])
    amounts.append(ind)
    i += ind
for j in range(len(numbers)):
    print(f"{numbers[j]} {amounts[j]}")
#===============S===============
text = input().split()
numbers, operations = [], []
for char in text:
    if char.isdigit():
        numbers.append(int(char))
    else:
        match char:
            case '*':
                numbers.append(numbers.pop() * numbers.pop())
            case '/':
                numbers.append(1 / numbers.pop() * numbers.pop())
            case '+':
                numbers.append(numbers.pop() + numbers.pop())
            case '-':
                numbers.append(-numbers.pop() + numbers.pop())
print(*numbers)
#===============T===============
from math import factorial

text = input().split()
numbers, operations = [], []
for char in text:
    if char.isdigit():
        numbers.append(int(char))
    else:
        match char:
            case '*':
                numbers.append(numbers.pop() * numbers.pop())
            case '/':
                numbers.append(1 / numbers.pop() * numbers.pop())
            case '+':
                numbers.append(numbers.pop() + numbers.pop())
            case '-':
                numbers.append(-numbers.pop() + numbers.pop())
            case '~':
                numbers.append(-numbers.pop())
            case '!':
                numbers.append(factorial(numbers.pop()))
            case '#':
                numbers.append(numbers[-1])
            case '@':
                third, second, first = numbers.pop(), numbers.pop(), numbers.pop()
                numbers.append(second)
                numbers.append(third)
                numbers.append(first)
print(*numbers)

