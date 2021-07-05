a = int(input())
b = int(input())
c = int(input())
if a==b and b==c:
    print("Все три числа имеют одинаковую величину ")
elif a < b:
    if a < c:
        print("Наименьшим из трех чисел является ",a)
    else:
        print("Наименьшим из трех чисел является ",с)
else:
        if b < c:
            print("Наименьшим из трех чисел является ",b)
        else:
            print("Наименьшим из трех чисел является ",c)