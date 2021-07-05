x_counter = {}
for i in range(int(input("Введите число строк:\n"))):
    string = input ("Введите очередную строку, ввод завершайте клавишей Enter\n").split()
    for word in string:
        x_counter[word] = x_counter.get (word,0)+1
max_counter = max (x_counter.values())
most_frequent = [k for k, v in x_counter.items() if v == max_counter]
print(min(most_frequent))
