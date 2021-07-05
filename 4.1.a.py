x = input("Введите целые числа через пробел, ввод завершите клавишей Enter:\n")
file = open ("list1.txt", "w", encoding = "utf-8")
file.write (x)
file.close ()

file = open ("list1.txt", "r", encoding = "utf-8")
x2 = file.read().split()
file.close ()

for i in range (len(x2)):
    x2[i] = int (x2[i])

x3=list()
for i in range (1,len(x2)):
    if i%2!=0:
        x3.append(x2[i])

file2 = open ("list2.txt", "w", encoding = "utf-8")
file2.write (str(x3))
file.close ()







