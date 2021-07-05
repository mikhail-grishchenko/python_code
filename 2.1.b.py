def dictionary (number):
  a = ''
  if number >= 1000:
    while number >= 1000:
      number -= 1000
      a += "M"
  elif number == 900:
    a += "CM"
  elif number == 800:
    a += "DCCC"
  elif number == 700:
    a += "DCC"
  elif number == 600:
    a += "DC"
  elif number == 500:
    a += "D"
  elif number == 400:
    a += "CD"
  elif number == 300:
    a += "CCC"
  elif number == 200:
    a += "CC"
  elif number == 100:
    a += "C"
  elif number == 90:
    a += "XC"
  elif number == 80:
    a += "LXXX"
  elif number == 70:
    a += "LXX"
  elif number == 60:
    a += "LX"
  elif number == 50:
    a += "L"
  elif number == 40:
    a += "XL"
  elif number == 30:
    a += "XXX"
  elif number == 20:
    a += "XX"
  elif number == 10:
    a += "X"
  elif number == 9:
    a += "IX"
  elif number == 8:
    a += "VIII"
  elif number == 7:
    a += "VII"
  elif number == 6:
    a += "VI"
  elif number == 5:
    a += "V"
  elif number == 4:
    a += "IV"
  elif number == 3:
    a += "III"
  elif number == 2:
    a += "II"
  elif number == 1:
    a += "I"
  return a

def translate (z):
  n3 = z % 10
  n2 = z % 100 - n3
  n1 = z % 1000 - n3 - n2
  n0 = z % 10000 - n3 - n2 - n1
  m = ''
  if n0 > 0:
    m += dictionary(n0)
  if n1 > 0:
    m += dictionary(n1)
  if n2 > 0:
    m += dictionary(n2)
  if n3 > 0:
    m += dictionary(n3)
  return m


try:
  z = int (input("Введите натуральное число в арабской нумерации в пределах от 1 до 3999\n"))
  if z <= 3999:
    print("Число в римской нуммерации - ", translate(z), "\n")
  else:
    print("Вы ввели некорректные данные")
except BaseException:
  print("Вы ввели некорректные данные")


