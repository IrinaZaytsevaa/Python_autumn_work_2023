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

