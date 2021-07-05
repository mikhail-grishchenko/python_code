def average_func(k):
    global h1
    global n1
    h1 += k2[t1][4]
    n1 += 1
    average = h1 / n1
    print("Средний балл по группе №", k2[t1][3], "равен:", average)

try:
    x_stud = int (input("Введите общее количество студентов:"))
except BaseException:
    print("\nВы ввели некорректные данные")
else:
    z = tuple()
    k1 = tuple()
    if x_stud > 0:
        print("Введите данные в следющем порядке: фамилию, имя, отчество, номер группы (1-59), средний балл.\nВсе данные вводите через пробел, завершайте ввод данных по каждому студенту клавишей Enter.")
        while x_stud > 0:
            try:
                f, i, o, n, b = input().split()
            except BaseException:
                print("\nВы ввели некорректные данные")
            else:
                try:
                    f, i, o = str(f), str(i), str(o)
                    n, b = int(n), int(b)
                except BaseException:
                    print("\nВы ввели некорректные данные")
                else:
                    if n <= 59:
                        m = tuple()
                        m += (f, i, o, n, b,)
                        k1 += (m,)
                        z += (b,)
                        x_stud -= 1
                    else:
                        print("\nВы ввели некорректные данные")

        k2 = sorted(k1, key = lambda k1: k1[3])
        h1 = 0
        n1 = 0
        t1 = 0
        while t1 < len (k2):
            if t1 == len(k2) - 1:
                if k2[t1][3] == k2[t1 - 1][3]:
                    average_func(k2)
                    h1 = 0
                    n1 = 0
                elif k2[t1][3] != k2[t1 - 1][3]:
                    h1 = 0
                    n1 = 0
                    average_func(k2)
            elif k2[t1][3]==k2[t1+1][3]:
                h1 += k2[t1][4]
                n1 += 1
            elif k2[t1][3]<k2[t1+1][3]:
                average_func(k2)
                h1 = 0
                n1 = 0
            t1 += 1
    else:
        print("\nВы ввели некорректные данные")
