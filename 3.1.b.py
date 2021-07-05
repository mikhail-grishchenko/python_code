def cut_begin_end_num(a):
    x = 0
    b = 0
    y = a
    while y >10:
        y = y // 10        
        x += 1
    b = (a-y*10**x)//10
    return b
print("Введите любое число больше 99")
a = int(input())
if a>99:
  print(cut_begin_end_num(a))
elif a<99:
  print("Вы ввели неверное число")

