def tabl_one (a, b):
  while b <= 10:
    z = print (a, " х ", b, " = ", a * b)
    b+=1    
#return 

def tabl_all(a, b):
  while a <= 9:
    tabl_one (a, b)
    print('\n')
    a+=1
#return


a, b = 2, 1
print (tabl_all(a, b))