lst = [23, 845, 69, -39, 74, 3, -1975]
current = 0
for i in lst:
    if i < current:
        current = i
print(current)