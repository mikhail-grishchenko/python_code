a = int(input())
b = int(input())
if a > b:
    dlina1 = a
    shirina1 = b
if a < b:
    shirina1 = a
    dlina1 = b

a1 = n1 = shirina1
while (n1 <= dlina1):
    print(a1, " ", a1)
    n1 += shirina1

shirina2 = dlina1 % shirina1
dlina2 = shirina1
a2 = n2 = shirina2
while (shirina2 > 0 and n2 <= dlina2):
    print(a2, " ", a2)
    n2 += shirina2

if shirina2 > 0:
    shirina3 = dlina2 % shirina2
    dlina3 = shirina2
    a3 = n3 = shirina3
    while (shirina3 > 0 and n3 <= dlina3):
        print(a3, " ", a3)
        n3 += shirina3

