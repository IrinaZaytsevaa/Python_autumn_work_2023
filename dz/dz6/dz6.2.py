books_first = input().replace(' ', '').split(',')
books_second = input().replace(' ', '').split(',')

my_lis = []
for book in books_first:
    if book in books_second:
        my_lis.append(book)
print(len(my_lis))





s = set(input().split(','))
z = set(input().split(','))
print(len(s.intersection(z)))
