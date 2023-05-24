a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5 ) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5 ) / (2 * a)
x1 = round(x1, 2)
x2 = round(x2, 2)
if d > 0:
    if x1 > x2:
       print(x2, x1)
    else:
        print(x1, x2)
elif d == 0:
    print(x1)
elif d < 0:
    print('No solution')
