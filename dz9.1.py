# gens = {'C': 'G', 'G': 'C', 'A': 'T', 'T': 'A'}
# s = input()
# res =''
# for i in s:
#     res += gens[i]
# print(res)




gens = {'C': 'G', 'G': 'C', 'A': 'T', 'T': 'A'}
def dnk_rnk(s):
    res =''
    for i in s:
        res += gens[i]
    return(res)
print(dnk_rnk(input()))