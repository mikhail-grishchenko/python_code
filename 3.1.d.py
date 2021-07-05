def sum_delit (a):
  sum_of_dividers = 0
  for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        sum_of_dividers += i
  return sum_of_dividers

numb = int(input("Введите целое число: "))
print ("Сумма делителей:",sum_delit (numb))


