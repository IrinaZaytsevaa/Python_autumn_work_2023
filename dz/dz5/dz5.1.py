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



n = int(input())
lst1 = [0, 1]
for i in range(1, n + 1):
    lst2 = [0]
    for j in range(i):
        lst2.append(lst1[j] + lst1[j + 1])
        print(lst2[-1], end='')
    lst2.append(0)
    print()
    lst1 = lst2.copy()



n = int(input())
lst = [0, 1, 0]
print(1)
for i in range(2, n + 1):
    x = lst[0]
    for j in range(1, i + 1):
        y = x + lst[j]
        lst[j] = y
    print()
    lst.append(0)