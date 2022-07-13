str = "Aubaid Nabi Lone"
def string_lenth(str):
    if str == '':
        return 0
    else :
        return 1 + string_lenth(str[1:])    

print(string_lenth(str))
