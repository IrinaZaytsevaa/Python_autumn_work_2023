def modify_genetic_code(code):
    new_code = ""
    i = 0
    while i < len(code):
        if i < len(code) - 1 and (code[i] == "А" and code[i+1] == "Г"):
            new_code += "ГА"
            i += 2
        elif i < len(code) - 1 and (code[i] == "Г" and code[i+1] == "А"):
            new_code += "АГ"
            i += 2
        elif i < len(code) - 1 and (code[i] == "Ц" or code[i] == "Т") and (code[i+1] == "Ц" or code[i+1] == "Т"):
            new_code += code[i] + "АГ" + code[i+1]
            i += 2
        else:
            new_code += code[i]
            i += 1
    return new_code


print(modify_genetic_code(input()))



