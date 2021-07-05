def answer (a):

  amount_of_dividers = 1
  answer_of_program = 0

  for i in range(numb, 1, -1):
    if (numb % i == 0):
        amount_of_dividers += 1

  if amount_of_dividers == 1:
    answer_of_program = -1
  elif amount_of_dividers == 2:
    answer_of_program = 1
  elif amount_of_dividers > 2:
    answer_of_program = 0
  return answer_of_program

numb = int(input("Введите целое число: "))
print ("Ответ программы:",answer (numb))