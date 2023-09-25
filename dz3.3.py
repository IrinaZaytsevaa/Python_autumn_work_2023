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








