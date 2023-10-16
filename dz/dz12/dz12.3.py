s = '1-2, 4-4, 3-6, 13-16'
def ranges(s):
    ranges_list = s.split(', ')
    lis = [num for r in ranges_list for num in (range(int(r.split('-')[0]), int(r.split('-')[1])+1) if '-' in r else [int(r)])]
    return lis

print(ranges(s))

# s = '1-2, 4-4, 3-6, 13-16'
# def ranges(s):
#     ranges_list = s.split(', ')
#     lis = []
#     for r in ranges_list:
#         if '-' in r:
#             start, end = map(int, r.split('-'))
#             lis.extend(list(range(start, end+1)))
#         else:
#             lis.append(int(r))
#     return lis
#
# print(ranges(s))


# import re
# def ranges(s):
#     ranges_list = re.findall(r'\d+', s)
#     lis = []
#     for i in range(0, len(ranges_list), 2):
#         lis.append((int(ranges_list[i]), int(ranges_list[i+1])))
#     return [i for j in lis for i in range(j[0], j[1] + 1)]
#
# input_str = '1-2, 4-4, 3-6, 13-16'
# print(ranges(input_str))

