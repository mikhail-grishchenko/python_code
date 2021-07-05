def sum_n (a):
  x=0
  while a>=1:
    x += a%10
    a = a//10        
  return x 

a = int (input())
print (sum_n(a))

