a = int(input())
max1_a = 0
max2_a = 0
while a!=0:
    if a > 0:
        if a > max1_a:
            max2_a = max1_a
            max1_a = a
        elif max2_a < a < max1_a:
            max2_a = a
    else:
        print("Введите только натуральные числа")
    a = int(input())
print("Значение второго по величине элемента ", max2_a)



