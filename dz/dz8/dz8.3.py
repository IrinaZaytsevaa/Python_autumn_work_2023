def sort_words(lst):
    lst = lst.split()
    lst.sort(key=lambda x: (-len(set(x)), x))
    return lst

print(sort_words(input()))
