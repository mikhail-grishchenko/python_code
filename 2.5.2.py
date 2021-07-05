x = set(input("Введите строку №1, ввод завершите клавишей Enter:\n").split())
y = set(input("Введите строку №2, ввод завершите клавишей Enter:\n").split())
z = x&y
a = list (z)
b = sorted(a, key=str.lower)
print ("Одинаковые слова в этих строчках, в алфавитном порядке:\n", b)


