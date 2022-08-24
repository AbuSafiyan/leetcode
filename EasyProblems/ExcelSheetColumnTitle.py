def convertToTitle(columnNumber):
    st = ''
    while columnNumber > 0:
        st = chr(ord('A') + (columnNumber - 1) % 26) + st
        columnNumber = (columnNumber - 1) // 26
    return st


a = 704
print(convertToTitle(a))
