import string
tt = str.maketrans(dict.fromkeys(string.punctuation))

file = open ("input.txt", "rt", encoding = "utf-8")
data = file.read().translate(tt).split()
file.close()

num_roman = list()
for i in data:
    try:
        num_roman.append (int (i))
    except BaseException:
        pass

sum_num_roman = sum (num_roman)
file2 = open ("output.txt", "wt", encoding = "utf-8")
file2.write (str(sum_num_roman))
file2.close()

