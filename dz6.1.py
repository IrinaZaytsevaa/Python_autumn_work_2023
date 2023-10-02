roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def convert_to_dec(integer):
    dec = 0
    for i, j in roman:
        while integer.startswith(j):
            dec += i
            integer = integer[len(j):]
    return dec
print(convert_to_dec(input()))