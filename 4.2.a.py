def fill (x,y):

    b = []
    d = 1

    for row in range (x):
        b.append([])
        for elem in range(y):
            b[row].append(0)

    end_circle_x, row_counter_x = x, x
    end_circle_y, column_counter_y = y, y
    start_circle_x = 0
    start_circle_y = 0

    while row_counter_x >= 1 and column_counter_y >= 1:
        for row_spiral in range (start_circle_x, end_circle_x):
            if row_spiral == start_circle_x: #заполняем первую строку вправо, проверив что это именно первая строка
                for elem_spiral in range(start_circle_y, end_circle_y):
                    b[row_spiral][elem_spiral] = d
                    d += 1
                row_counter_x -= 1
            elif start_circle_x < row_spiral < end_circle_x - 1: #заполняем в крайнем правом положении столбец вниз, проверив что это строки между первой и последней строкой очередного витка спирали
                b[row_spiral][end_circle_y-1] = d
                d += 1
                if row_spiral == end_circle_x-2:
                    column_counter_y -= 1
            elif row_spiral == end_circle_x - 1: #заполняем часть нижней строки и обращаем ее наоброт, проверив что это именно последняя строка витка спирали
                for elem_spiral in range(start_circle_y,end_circle_y):
                    b[row_spiral][elem_spiral] = d
                    d += 1
                b2 = b[row_spiral][start_circle_y:end_circle_y]
                b2.reverse()
                i = 0
                for elem_end_row in range(start_circle_y,end_circle_y):
                    b[row_spiral][elem_end_row] = b2[i]
                    i += 1
                row_counter_x -= 1
        if column_counter_y >= 1:
            for column_spiral_reverse in range(end_circle_x - 2, start_circle_x, -1): #заполняем первый столбец снизу вверх, проверив что столбцов больше одного
                b[column_spiral_reverse][start_circle_y] = d
                d += 1
            column_counter_y -= 1

        start_circle_x += 1
        start_circle_y += 1
        end_circle_x -= 1
        end_circle_y -= 1

    return b

x = int(input("Введите количество строк матрицы:\n"))
y = int(input("Введите количество столбцов матрицы:\n"))
print("Вывод матрицы:")
for i in fill(x, y):
    print(' '.join(map(str, i)))




#x= 1;  y =......11.протестировано
#x= .........11.; y =1 протестировано
#x= 2;  y =......11.протестировано
#x= .........11.; y =2.протестировано
#x= 3;  y =......11.протестировано
#x= .........11.; y =3 протестировано
#x= 4;  y =......11.протестировано
#x= .........11.; y =4 протестировано
#x= 5;  y =......11.протестировано
#x= .........11.; y =5 протестировано