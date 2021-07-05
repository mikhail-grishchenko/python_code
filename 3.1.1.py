def gcd (a, b):
  while b!=0:
    a, b = b, a%b
  return a 

x, y = int (input()), int (input())

while x!=0 and y!=0:
  x = gcd(x,y)
  y = int (input())   

print (gcd(x,y))


