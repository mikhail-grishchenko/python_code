import os
import string
import random

def id_generator(size, chars):
    return ''.join(random.choice(chars) for _ in range(size))

n=0
file = open ("doc3.txt", "w", encoding = "utf-8-sig")
while n<random.randrange(1, 200, 1):
    size = random.randrange(1, 30, 1)
    chars = string.ascii_uppercase + string.digits
    file.write("     ")
    file.write(id_generator(size, chars))
    file.write ("\n\n")
    n+=1
file.close ()

file2 = open ("doc3.txt", "r", encoding = "utf-8-sig")
x2 = file2.read()
file2.close ()

characters=0
for line in x2:
    line = line.strip(os.linesep)
    wordslist=line.split()
    for word in wordslist:
        characters+=sum(c != ' ' for c in word)
print(characters)


