from math import sqrt

a = 5
b = -10
c = 4

d = b**2 - 4 * a * c

if d < 0:
    print('корней нет')
elif d == 0:
    x = -b / (2 * a)
    print(f'корень 1 = {x}')
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1, x2)
    
