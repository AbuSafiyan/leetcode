def checkRecord(s):
    ab = s.count('A')
    la = s.count('LLL')
    if ab > 1 or la >= 3:
        return False
    return True


a = "PPAALLLP"
print(checkRecord(a))
