name = input()
price, weight, money = int(input()), int(input()), int(input())
value = price * weight
change = money - price * weight
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {value}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")