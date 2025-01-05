name = input()
price = int(input())
weight = int(input())
money = int(input())

price_str = f"{price}руб/кг"
weight_str = f"{weight}кг"
value_str = f"{weight * price}руб"
money_str = f"{money}руб"
change_str = f"{money - price * weight}руб"
second_str = f"{weight_str} * {price_str}"
print(f"{'Чек':=^35}")
print(f"{'Товар:': <17} {name: >17}")
print(f"{'Цена:': <17} {second_str: >17}")
print(f"{'Итого:': <17} {value_str: >17}")
print(f"{'Внесено:': <17} {money_str: >17}")
print(f"{'Сдача:': <17} {change_str: >17}")
print(f"{'=':=^35}")