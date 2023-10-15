n = int(input())
N = n * n
S = [[0 for i in range(n)] for j in range(n)]
a, i, j = 1, 0, 0
if N % 2 == 0:
    S[n // 2][n // 2] = N
    N -= 1
k = 0
while a <= N:
    for right in range(n - 1 - k):
        if a > n * n:
            break
        else:
            S[i][j] = a
            a += 1
            j += 1
    for down in range(n - 1 - k):
        if a > n * n:
            break
        else:
            S[i][j] = a
            a += 1
            i += 1
    for left in range(n - 1 - k):
        if a > n * n:
            break
        else:
            S[i][j] = a
            a += 1
            j -= 1
    for up in range(n - 1 - k):
        if a > n * n:
            break
        else:
            S[i][j] = a
            a += 1
            i -= 1
    i += 1
    j += 1
    k += 2
for i in S:
    for j in i:
        print(j, end=' ')
    print()










n = int(input())
m = {}
for i in range(n):
    for j in range(n):
        m[i, j] = 0
x, y, dx, dy = 0, 0, 0, 1
for k in range(1, n * n + 1):
    m[x, y] = k
    if m.get((x + dx, y + dy), -1) != 0:
        if (dx, dy) == (0, 1):
            dx = 1; dy = 0
        elif (dx, dy) == (1, 0):
            dx = 0; dy = -1
        elif (dx, dy) == (0, -1):
            dx = -1; dy = 0
        elif (dx, dy) == (-1, 0):
            dx = 0; dy = 1
    x += dx
    y += dy
len_n = len(str(n * n))
for i in range(n):
    for j in range(n):
        print(f"{m[i, j]:{len_n}}", end =' ')
    print()
