abcd = int(input())
a = abcd // 1000
b = abcd // 100 % 10
c = abcd // 10 % 10
d = abcd % 10
print(f"{b}{a}{d}{c}")