a = int(4)
b = int(1)
i = int(1)
sum_y = float(0)
while i <= 10:
    y = float(a/b)
    sum_y = sum_y+y
    b = (b + 2)
    i = i+1
else:
    print(sum_y)