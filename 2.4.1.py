L = input("Введите список через пробел, ввод завершите клавишей Enter:\n").split()
n = int(input("Введите число n:\n"))
i = 0
while i < len(L):
    L[i] = int (L[i])
    i+=1
L2 = []
for m in range (len(L)):
    if L[m] == n:
        L2.append (m)
print ("Число n содержится на данных позициях (индексах):", L2, "списка L")

