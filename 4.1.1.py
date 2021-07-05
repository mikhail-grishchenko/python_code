file = open ("doc.txt", "rt", encoding = "utf-8")
roman = ""
while True:
    line = file.readline()
    if not line:
        break
    roman += line
file.close()

file2 = open ("doc1.txt", "wt", encoding = "utf-8")
file2.write (roman)
file2.close()
