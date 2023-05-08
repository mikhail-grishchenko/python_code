# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
import math
area = round(math.pi*(radius**2),4)
print(area)

# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

hypotenuse = math.sqrt(point[0]** 2 + point[1] ** 2)
print(hypotenuse <= radius)

# Аналогично для другой точки
point_2 = (30, 30)

hypotenuse2 = math.sqrt(point_2[0]** 2 + point_2[1] ** 2)
print(hypotenuse2 <= radius)



