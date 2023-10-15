x, y = int(input()), int(input())
lis = [x + y, x - y, x * y, x / y, x // y]
lis.sort()
print('Второе наибольшее число =', lis[-2])



a, b, c, d, e = x + y, x - y, x * y, x / y, x // y
current, current1 = a, b
if a < b:
    current, current1 = b, a
if c > current:
    current, current1 = c, current
elif c > current1:
    current1 = c
if d > current:
    current, current1 = d, current
elif d > current1:
    current1 = d
if e > current:
    current, current1 = e, current
elif e > current1:
    current1 = e
print(current1)