def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
   
def func_float (a,b):
  a,b = float(a), float(b)
  return a+b

def func_str (a,b):
  a, b = str(a), str(b)
  return a+b

a = input()
b = input()

if is_float(a) == True and is_float(b) == True:
  print(func_float(a,b))
else:
  print(func_str(a,b))