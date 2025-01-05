name = input()
number = int(input())
group = number // 100
bed = number // 10 % 10
order = number % 10
print(f"Группа №{group}.")
print(f"{order}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {bed}.")