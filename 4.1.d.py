import string
import random

def id_generator(size, chars):
    return ''.join(random.choice(chars) for _ in range(size))

def delete_file(f):
    f2 = ""
    for i in f:
        if i != "-" and i != "+":
            f2+=i
        else:
            pass
    return f2

n=0
file = open ("doc4.txt", "w", encoding = "utf-8-sig")
while n<random.randrange(10, 200, 1):
    size = random.randrange(10, 30, 1)
    chars = string.punctuation
    file.write("     ")
    file.write(id_generator(size, chars))
    file.write ("\n\n")
    n+=1
file.close ()

with open ("doc4.txt", "r", encoding = "utf-8-sig") as file2:
    f = file2.read()

with open ("doc4.txt", "w", encoding = "utf-8-sig") as file2:
    file2.write(delete_file(f))

