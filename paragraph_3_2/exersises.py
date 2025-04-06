# ===============A===============
word = set(input())
for i in word:
    print(f"{i}", end="")
# ===============B===============
result = set(input()) & set(input())
for i in result:
    print(f"{i}", end="")
# ===============C===============
result = set()
for _ in range(int(input())):
    text = list(input().split())
    for word in text:
        result.add(word)
for i in result:
    print(f"{i}")

# ===============D===============
n, m = int(input()), int(input())
ovsyan, mannaya = set(), set()
for _ in range(n):
    mannaya.add(input())
for _ in range(m):
    ovsyan.add(input())
if not len(ovsyan & mannaya):
    print("Таких нет")
else:
    print(len(ovsyan & mannaya))
# ===============E===============
n, m = int(input()), int(input())
ovsyan, mannaya = set(), set()
for _ in range(n + m):
    name = input()
    if name in ovsyan:
        mannaya.add(name)
    else:
        ovsyan.add(name)
if not len(ovsyan ^ mannaya):
    print("Таких нет")
else:
    print(len(ovsyan ^ mannaya))
# ===============F===============
n, m = int(input()), int(input())
ovsyan, mannaya = set(), set()
for _ in range(n):
    mannaya.add(input())
for _ in range(m):
    ovsyan.add(input())
result = list(ovsyan ^ mannaya)
if not len(result):
    print("Таких нет")
else:
    result.sort()
    for child in result:
        print(child)
# ===============G===============
morze = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'}
words = input().split()
for word in words:
    word_up = word.upper()
    for char in word_up:
        print(f"{morze[char]}", end=" ")
    print()

# ===============H===============
childrens, result = dict(), list()
for _ in range(int(input())):
    string = input().split()
    childrens[f"{string[0]}"] = []
    for i in range(1, len(string)):
        childrens[f"{string[0]}"].append(string[i])
porridge = input()
for key, value in childrens.items():
    if porridge in value:
        result.append(key)
result.sort()
if not len(result):
    print("Таких нет")
else:
    for child in result:
        print(child)


# ===============I===============
nature = dict()
while (string := input()) != "":
    string = string.split()
    for living in string:
        nature[living] = nature.get(living, 0) + 1
for key, values in nature.items():
    print(f"{key} {values}")

# ===============J===============
translit = {
    'а': 'a', 'б': 'b', 'в': 'v',
    'г': 'g', 'д': 'd', 'е': 'e',
    'ё': 'e', 'ж': 'zh', 'з': 'z',
    'и': 'i', 'й': 'i', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'tc',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ы': 'y', 'э': 'e', 'ю': 'iu',
    'я': 'ia', ' ': ' ', 'ъ': '',
    'ь': ''
}
result = ""
for char in input():
    if char.lower() in translit:
        result += str(translit.get(char.lower())).capitalize() if char.isupper() else str(translit.get(char))
    else:
        result += char
print(result)
# ===============K===============
employees = dict()
result = 0
for _ in range(int(input())):
    employee = input()
    employees[employee] = employees.get(employee, 0) + 1
for value in employees.values():
    if value > 1:
        result += value
print(result)

# ===============L===============
employees = dict()
result = False
for _ in range(int(input())):
    employee = input()
    employees[employee] = employees.get(employee, 0) + 1
employees = dict(sorted(employees.items()))
for key, value in employees.items():
    if value > 1:
        print(f"{key} - {value}")
        result = True
if not result:
    print("Однофамильцев нет")

# ===============M===============
today = set()
past = set()
for _ in range(int(input())):
    today.add(input())
for _ in range(int(input())):
    for _ in range(int(input())):
        past.add(input())
result = sorted(list(today - past))
if not len(result):
    print("Готовить нечего")
else:
    print(*result, sep='\n')
# ===============N===============
products = set()
receipts = dict()
flag = False
for _ in range(int(input())):
    products.add(input())
for _ in range(int(input())):
    dish = input()
    for _ in range(int(input())):
        receipts[dish] = set(list(receipts.get(dish, [])) + [input()])
receipts = dict(sorted(receipts.items()))
for key, value in receipts.items():
    if products >= value:
        print(key)
        flag = True
else:
    if not flag:
        print("Готовить нечего")
# ===============O===============
data_in = list(map(bin, list(map(int, input().split()))))
data_in = list(map(lambda x: x[2:], data_in))
result = list()
for num in data_in:
    num_info = dict()
    num_info["digits"] = len(num)
    for digit in num:
        if digit == '1':
            num_info["units"] = int(num_info.get("units", 0)) + 1
        else:
            num_info["zeros"] = int(num_info.get("zeros", 0)) + 1
    # Надо добавить, тк если все 1 или 0, то будет отсуствовать num_info["zeros"] или num_info["units"]
    num_info["units"] = num_info.get("units", 0)
    num_info["zeros"] = num_info.get("zeros", 0)
    result.append(num_info)
print(result)
# ===============P===============
around = set()
while (line := input()) != "":
    line = line.split()
    step1 = True
    step2 = True
    while "зайка" in line:
        if not line.index("зайка"):
            step2 = False
        if line.index("зайка") == len(line) - 1:
            step1 = False
        if step1:
            around.add(line[line.index("зайка") + 1])
        if step2:
            around.add(line[line.index("зайка") - 1])
        line.remove("зайка")
else:
    print(*around, sep='\n')
# ===============Q===============
friends = dict()
result = dict()
# Парсим входные данные
while (line := input()) != "":
    line = line.split()
    friends[line[0]] = set(list(friends.get(line[0], [])) + [line[1]])
    friends[line[1]] = set(list(friends.get(line[1], [])) + [line[0]])
# Формируем список вторых рукопожатий
for key, value in friends.items():
    for friend in value:
        friend_set = friends[friend] - set([key])
        result[key] = sorted(list(set(result.get(key, {})) | friend_set - value))
result = dict(sorted(result.items()))
# Вывод
for key, value in result.items():
    string = ""
    for name in value:
        string += name + ', '
    print(f"{key}: {string[:-2]}")
# ===============R===============
# Превышен лимит (1с)
points = list()
max_len = 0
for _ in range(int(input())):
    point = tuple(input().split())
    points.append(point)
for point_1 in points:
    count = 0
    for point_2 in points:
        if point_1 != point_2 and point_1[0][:-1] == point_2[0][:-1] and point_1[1][:-1] == point_2[1][:-1]:
            count += 1
    max_len = max(count + 1, max_len)
print(max_len)

# ===============S===============
# Проходит не все тесты
toys, names = dict(), list()
res, delete = set(), set()
for _ in range(int(input())):
    string = (input().split())
    for word in string:
        if ":" in word:
            name = word.rstrip(":")
            names.append(name)
        else:
            word = word.rstrip(",")
            toys[name] = set(list(toys.get(name, {})) + [word])
for value in toys.values():
    delete = value if not len(delete) else delete & value
    res = value if not len(res) else res ^ value
res = sorted(list(res - delete))
print(*res, sep="\n")
# ===============T===============
numbers = sorted(list(set(map(int, input().split("; ")))))
nods = dict()
res = dict()
# создаем словарь - число из списка: [список его делителей]
for num in numbers:
    nod = []
    for i in range(1, num + 1):
        if num % i == 0:
            nod.append(i)
    nods[num] = set(nod)
# формируем словарь ответа - число : [числа, которых нет в списке его делителей]
for key, value in nods.items():
    for num in numbers:
        if len(value & nods[num]) == 1:
            res[key] = res.get(key, []) + [num]
# форматированный вывод
for key, value in res.items():
    string = ""
    if len(value):
        for num in value:
            string += str(num) + ", "
        print(f"{key} - {string[:-2]}")
