string = input()
n = int(input())
lis = []
def code(string, n):
    for word in string:
        if word.isalpha():
            lis.append(chr(ord(word) + n))
        else:
            lis.append(word)
    return lis
print(*code(string, n))