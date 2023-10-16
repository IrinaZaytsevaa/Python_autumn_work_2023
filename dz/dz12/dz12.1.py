lis = [1, 2, 3, 1, 4, 4, 2, 1, 4, 1, 2]
def lists(lis):
    return [i for i, j in enumerate(lis) if j == min(lis)], [i for i, j in enumerate(lis) if j == max(lis)]

print(*lists(lis), sep=', ')

