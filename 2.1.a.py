def string (z):
  a = ''
  b = ''
  for i in range (len(z)):
    a += z[i] + "*"
  b = a[:len(a)-1]
  return b

z = str (input())
print (string (z))