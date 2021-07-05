x = set(input("Введите список №1 с числами через пробел, ввод завершите клавишей Enter:\n").split())
y = set(input("Введите список №2 с числами через пробел, ввод завершите клавишей Enter:\n").split())
z = x.symmetric_difference(y)
a = list (z)
b = sorted(a, key=str.lower)
print ("Числа, которые входят только в один список:\n", b)


