#Вариант в одну строку
print(max(input().split(), key=len))



#второй вариант, подлиннее
sentence = input().split()
ls = []
k = ''
for word in sentence:
    ls.append(len(word))
    k = ls.index(max(ls))
print(sentence[k])


#решение с несколькими наибольшими словами

sentence = input().split()
ls = []
lis = []
for word in sentence:
    ls.append(len(word))
for w in sentence:
    if max(ls) == len(w):
        lis.append(w)

print(*lis)







