x = input("Введите список через пробел, ввод завершите клавишей Enter:\n").split()
c = x[len (x) - 1]
d = x [0]
i=-1
while i > -(len (x) - 1) :
    x[i] = x [i-1]
    i-=1
x[0] = c
x[1] = d
print ("Измененный список:\n", x)

