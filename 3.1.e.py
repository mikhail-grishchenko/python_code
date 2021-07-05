def inverted_num (a):
  inverted_n1 = 0
  n =  1
  b = a
  
  while b>=10:
    b = b//10
    n *= 10
   
  while a>=1:
    inverted_n1 += int (a%10 * n)
    n=n/10 
    a = a//10
  
  return inverted_n1


numb = int (input("Введите целое число: "))
print ("Перевернутая запись:", inverted_num (numb)  )
