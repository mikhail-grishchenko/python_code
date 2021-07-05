def string (z):
  a=''
  b=''
  in_t = 0
  for i in range (len(z)):
    try:
      in_t = int (z[i])
      if in_t == 1:
        a = "one"
      else:
        a = z[i]
    except Exception:
        a = z[i]
    b += a   
  return b

z = str (input())
print (string (z))


