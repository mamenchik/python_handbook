name = input()
price = int(input())
weight = int(input())
money = int(input())
value = price * weight
change = money - price * weight
print("Чек")
print(name, " - ", weight, "кг - ", price, "руб/кг", sep="")
print("Итого: ", value, "руб", sep="")
print("Внесено: ", money, "руб", sep="")
print("Сдача: ", change, "руб", sep="")