x, y = int(input()), int(input())
print('Наибольшее число =', max(x + y, x - y, x * y, x / y, x // y))


a, b, c, d, e = x + y, x - y, x * y, x / y, x // y
current = a
if b > current:
    current = b
if c > current:
    current = c
if d > current:
    current = d
if e > current:
    current = e
print(current)