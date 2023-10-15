s = input().split()
my_list, k = [], ''
for i in s:
    if i.isdigit():
        my_list.append(i)
    else:
        k = i
a, b = int(my_list[0]), int(my_list[1])
if k == '+':
    print(a + b)
if k == '-':
    print(a - b)
if k == '*':
    print(a * b)
if k == '/':
    print(a / b)



s = input().split()
a, b = int(s[0]), int(s[2])
if s[1] == '+':
    print(a + b)
elif s[1] == '-':
    print(a - b)
elif s[1] == '*':
    print(a * b)
elif s[1] == '/':
    print(a / b)


s = input().split()
a, b = int(s[0]), int(s[2])
dct = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
print(dct[s[1]])

#решение с помощью словаря
