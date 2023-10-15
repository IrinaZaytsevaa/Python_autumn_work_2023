fib1, fib2 = 1, 1
n = int(input())
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')




n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
    print(a, end=' ')