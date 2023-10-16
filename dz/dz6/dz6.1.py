roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def convert_to_dec(integer):
    dec = 0
    for i, j in roman:
        while integer.startswith(j):
            dec += i
            integer = integer[len(j):]
    return dec
print(convert_to_dec(input()))




def roman_to_decial(number):
    dct = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    while number != '':
        for i in dct:
            if number.startswith(i):
                res += dct[i]
                number = number[len(i):]
                break
    return res
print(roman_to_decial(input()))