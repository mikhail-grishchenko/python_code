n, m = [int(elem) for elem in input("Введите количество строк и столбцов матрицы через пробел, для завершения ввода жмите Enter:\n").split()]

matrix = []

for row in range(n):
    matrix.append([])
    for elem in range(m):
        matrix[row].append(".")

for row2 in range(n):
    if row2%2==0:
        for elem2 in range(m):
            if elem2%2>0:
                matrix[row2][elem2] = "*"
    else:
        for elem2 in range(m):
            if elem2%2==0:
                matrix[row2][elem2] = "*"

for elem3 in matrix:
    print(' '.join(map(str, elem3)))

