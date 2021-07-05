n = int(input())
f1 = f2 = 1
i = 1
s = 0
print(f1)
while (i < n):
    s = f1 + f2
    f1 = f2
    f2 = s
    i += 1
    print(s)
