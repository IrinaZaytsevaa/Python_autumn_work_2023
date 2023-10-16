n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = ' ')



n = int(input())
k = 2
dct ={}
while n > 1:
    while n % k == 0:
        dct[k] = dct.get(k, 0) + 1
        n //= k
    k += 1
for k in dct:
    print(k, dct[k])
