def subt (x,y,a,b):

    subt_matrix = []
    for row in range(x):
        subt_matrix.append([])
        for elem in range(y):
            subt_matrix[row].append(0)

    for row2 in range(len(a)):
        for elem2 in range(len(a[0])):
            subt_matrix[row2][elem2] = a[row2][elem2] - b[row2][elem2]

    return subt_matrix

x = int(input("Введите количество строк матриц:\n"))
y = int(input("Введите количество столбцов матриц:\n"))

a = []
print("Введите через пробел элементы матрицы №1, для завершения ввода строки нажмите Enter:\n")
for i in range (x):
    a.append([int(j)for j in input().split()])

b = []
print("Введите через пробел элементы матрицы №2, для завершения ввода строки нажмите Enter:\n")
for i in range (x):
    b.append([int(j)for j in input().split()])

print("Результат вычитания из первой матрицы второй:\n")
for elem3 in subt(x,y,a, b):
    print(' '.join(map(str, elem3)))













