# Excel Sheet Column Number

def titleToNumber(columnTitle):
    res = 0
    for i in columnTitle:
        res = res * 26 + ord(i) - 64

    return res


a = 'LEET'
print(titleToNumber(a))
