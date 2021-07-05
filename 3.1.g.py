def prost_num (a, b):
  for i in range(a, b):
    s = 0
    for j in range(1, int(i // 2) + 1):
        if i % j == 0:
            s += j
    if s != i:
      print(i, end = ",") 

a = int (input())
b = int (input())
prost_num(a, b)