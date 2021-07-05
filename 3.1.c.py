def cut_begin_end_num(a):
    x = 0
    b = 0
    y = a
    while y >10:
        y = y // 10        
        x += 1
    b = (a-y*10**x)//10
    c = (b + 9*10**(x-1))*10
    return c
print("Введите любое число больше 9")
a = int(input())
if a>9:
  print(cut_begin_end_num(a))
elif a<9:
  print("Вы ввели неверное число")
