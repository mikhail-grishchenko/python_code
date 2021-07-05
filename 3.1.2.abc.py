def len (x_1:float, y_1: float, x_2: float, y_2: float):
  return ((x_2-x1)**2+(y_2-y_1)**2)**0.5

def square (x_1:float, y_1: float, 
            x_2: float, y_2: float,
            x_3: float, y_3: float):
    a = len (x_1, y_1, x_2, y_2)
    b = len (x_1, y_1, x_3, y_3)
    c = len (x_2, y_2, x_3, y_3)
    p = a + b + c
    p_2 = p/2
    square_t = (p_2 * (p_2-a)*(p_2-b)*(p_2-c))**0.5
    return square_t

x1 = float (input())
y1 = float (input())
x2 = float (input())
y2 = float (input())
x3 = float (input())
y3 = float (input())
s = square(x1, y1, x2, y2, x3, y3)
print ('{0:10.6f}'.format(s))