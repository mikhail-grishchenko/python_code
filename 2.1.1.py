def string (z):
  a=''
  b=''
  c=''
  for i in range (len(z)//2+len(z)%2):
      a += z[i]
  b = z[len(z)//2+len(z)%2:len(z)]
  c = b+a
  return c

z = str (input())
print (string (z))