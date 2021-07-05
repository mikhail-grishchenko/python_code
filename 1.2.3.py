print ("Клетки поля имеют значения от 1 до 8")
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if 1<= x1 <= 8 and 1<= y1 <= 8 and 1<= x2 <= 8 and 1<= y2 <= 8:
    x = abs(x1 - x2)
    y = abs(y1 - y2)

    if x == y :
        print ("YES")
    else:
        print ("NO")
