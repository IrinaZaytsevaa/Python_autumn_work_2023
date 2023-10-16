# s = '1-2, 4-4, 3-6'.split(',')
# s = ''.join(s).replace('-', '').split()
# lis, final = [], []
#
# for i in s:
#     i = tuple(i)
#     lis.append(i)
#
# def ranges(lis):
#     for j in lis:
#         for i in range(int(j[0]), int(j[1]) + 1):
#             final.append(i)
#     return final
#
# print(ranges(lis))

s = '1-2, 4-4, 3-6'.split(',')
s = ''.join(s).replace('-', '').split()
lis = []

for i in s:
    i = tuple(i)
    lis.append(i)

def ranges(lis):
    return [i for j in lis for i in range(int(j[0]), int(j[1]) + 1)]

print(ranges(lis))