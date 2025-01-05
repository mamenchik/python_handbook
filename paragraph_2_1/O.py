hours = int(input())
minutes = int(input())
delivery = int(input())
time = hours * 60 + minutes + delivery
clock_h = int((int(time / 60)) % 24)
clock_m = time % 60
if (clock_h > 10):
    if clock_m > 10:
        print(f"{clock_h}:{clock_m}")
    else:
        print(f"{clock_h}:0{clock_m}")
else:
    if clock_m > 10:
        print(f"0{clock_h}:{clock_m}")
    else:
        print(f"0{clock_h}:0{clock_m}")
