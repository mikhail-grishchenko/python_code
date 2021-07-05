file = open ("doc.txt", "rt", encoding = "utf-8")
data = file.read().split()
print (len(data))
file.close()


