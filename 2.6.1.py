import string
tt = str.maketrans(dict.fromkeys(string.punctuation))
x1 = list ((input("Введите список слов через пробел, ввод завершите клавишей Enter:\n").translate(tt)).split())
for i in range(len(x1)):
    x1[i] = x1[i].lower()
x2 = list (x1[0].split())
y = {}
y ['1.'+x1[0]] = 0
n = 2
for i in range(1,len(x1)):
    y[str(n) + '.' + x1[i]] = x2.count (x1[i])
    n += 1
    x2.append (x1[i])
print ("Все слова выведены со своим порядковым номером, после знака двоеточие выведено количество раз, \n "
       "сколько это слово встречалось ранее в тексте, все слова приведены к одному регистру:\n",y)




