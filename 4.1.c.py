x2 = []

file = open ("doc.txt", "r", encoding = "utf-8-sig")
while True:
    line = file.readline()
    if not line:
        break
    x2.append(line)
file.close ()

x2_reverse = x2[::-1]

file2 = open ("doc4.txt", "w", encoding = "utf-8-sig")
for line in x2_reverse:
    file2.write(line)
file2.close ()





