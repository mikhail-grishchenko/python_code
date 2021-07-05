a = int(input())
min_a = 0
max_a = 0
while a != 0:
    if a > max_a:
        max_a = a
    elif a < min_a:
        min_a = a
    a = int(input())
print("Минимум равен ", min_a)
print("Максимум равен ", max_a)





