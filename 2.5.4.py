x = list(input("Введите список с числами через пробел, ввод завершите клавишей Enter:\n").split())
y = []
y.append(x[0])
a = ['NO',]

for i in range(1,len(x)):
    if x[i] in y:
        a.append('YES')
    else:
        a.append('NO')
    y.append(x[i])

print(a)


