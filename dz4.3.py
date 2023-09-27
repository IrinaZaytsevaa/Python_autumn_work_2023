sentence1 = input().split()
sentence2 = input().split()
lis1, lis2 = [], []
for word in sentence1:
    for i in word:
        if i.isalpha():
            lis1.append(i.lower())
for word in sentence2:
    for j in word:
        if j.isalpha():
            lis2.append(j.lower())
def sortByAlphabet(inputStr):
    return inputStr[0]
lis1.sort(key=sortByAlphabet)
lis2.sort(key=sortByAlphabet)
print(lis1 == lis2)
