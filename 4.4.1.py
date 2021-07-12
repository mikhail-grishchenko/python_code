n, m = [int(elem) for elem in input("Введите количество строк и столбцов матрицы через пробел, для завершения ввода жмите Enter:\n").split()]
print("Введите через пробел элементы строки матрицы, для завершения ввода строки нажмите Enter:\n")
a = [[int(elem2) for elem2 in input().split()] for i in range(n)]

result_i, result_j = 0, 0
current_elem = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > current_elem:
            current_elem = a[i][j]
            result_i, result_j = i, j
print("Индексы первого вхождения максимального элемента:\n", result_i, result_j)
