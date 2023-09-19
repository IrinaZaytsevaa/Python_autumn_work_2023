x, y = int(input()), int(input())
lis = [x + y, x - y, x * y, x / y, x // y]
lis.sort()
print('Второе наибольшее число =', lis[-2])