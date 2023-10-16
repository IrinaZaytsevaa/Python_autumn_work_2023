def sort_lists(lst):
    lst.sort(key=lambda x: sum([len(str(i)) for i in x]))
    for sublist in lst:
        sublist.sort(reverse=True)
    return lst



input_lst = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]
output = sort_lists(input_lst)
print(sort_lists(output))
