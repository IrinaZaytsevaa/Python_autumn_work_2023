s = input()
my_set1, my_set2, my_set3 = set(), set(), set()
for i in s:
    if i.isdigit():
        my_set1.add(i)
    elif i.isalpha():
        my_set2.add(i)
    else:
        my_set3.add(i)

print(*my_set2)
print(*my_set1)
print(*my_set3)