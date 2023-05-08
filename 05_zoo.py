# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1,'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
# for elem in birds:
#     zoo.append(elem)
print(zoo)
# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
# del zoo[3]
# zoo.pop(3)
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
for elem in zoo:
    if elem =='lion' or elem =='lark':
        print(zoo.index(elem)+1)


