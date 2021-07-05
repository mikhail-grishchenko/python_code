def tuple_func():
    a = int(input("Введите число:"))
    b = tuple()
    while (a != 0):
        b += (a,)
        a = int(input("Введите число:"))
    d = (min(b), max(b))
    return d

try:
    print ("Вводите через Enter натуральные числа, для завершения введите 0")
    print("Минимум и максимум значений из введенной последовательности чисел (данного кортежа):",tuple_func())
except BaseException:
    print("Вы ввели некорректные данные")

