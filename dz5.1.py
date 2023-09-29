n = int(input())
lst = []
for i in range(0, n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
    lst.append(row)
for r in lst:
    print(*r)