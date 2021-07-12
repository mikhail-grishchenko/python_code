def sum (x,y,a,b):

    sum_matrix = []
    for row in range(x):
        sum_matrix.append([])
        for elem in range(y):
            sum_matrix[row].append(0)

    for row2 in range(len(a)):
        for elem2 in range(len(a[0])):
            sum_matrix[row2][elem2] = a[row2][elem2] + b[row2][elem2]

    return sum_matrix

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

print("Суммарная матрица:\n")
for elem3 in sum(x,y,a, b):
    print(' '.join(map(str, elem3)))













