def tuple_func (a):
    b = tuple(i for i in range(1, a+1))
    return b

try:
    a = int (input("Введите натуральное число \n"))
except BaseException:
    print("Вы ввели некорректные данные")
else:
    print (tuple_func(a))