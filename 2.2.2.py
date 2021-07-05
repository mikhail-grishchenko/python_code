def tuple_func(d):
    a = tuple() + tuple(int(i) for i in d.split(","))
    b, c1, c2 = 0, 0, 0
    while b < len(a)-1:
        if a[b] <= a[b+1]:
            c1 = 1
        elif a[b] > a[b+1]:
            c2 = 1
        b+=1
    if c1>c2:
        print("Кортеж упорядочен по возрастанию")
    elif c1<=c2:
        print("Кортеж не упорядочен по возрастанию")

try:
    d = input("Введите через запятую натуральные числа \n")
    tuple_func(d)
except BaseException:
    print("Вы ввели некорректные данные")

