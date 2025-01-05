number = int(input())
digit1 = number // 1000
digit2 = number // 100 % 10
digit3 = number // 10 % 10
digit4 = number % 10
print(f"{digit2}{digit1}{digit4}{digit3}")