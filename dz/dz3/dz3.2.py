num = [int(i) for i in input()]
for j in range(10):
    k = num.count(j)
    print(f'{j} - {k}', sep = '\n')


#решение в классе
s = input()
res = [0] * 10
for k in s:
    i = int(k)
    res[i] += 1
for j in range(10):
    print(f'{j} - {res[j]}')



