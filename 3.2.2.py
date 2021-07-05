def param_func(args):
    b, c, r = 0, 0, 0
    for e in args:
        r += e
        c+=1
    average = r/c
    return average

try:
    f = tuple()
    a = int(input("Введите через Enter произвольное количество целых чисел (параметров) до 0 :\n"))
    while a!=0:
        f += (a,)
        a = int(input())
    print ("Среднее арифметическое данных чисел:",param_func(f))
except BaseException:
    print("Вы ввели некорректные данные")


