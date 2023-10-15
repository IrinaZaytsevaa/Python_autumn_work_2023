s = input()
dct = {}
for i in s:
    dct[i] = dct.get(i, 0) + 1
lst = sorted(dct, key = lambda x: (-dct[x], x))
for i in lst[:10]:
    print(i, dct[i])
