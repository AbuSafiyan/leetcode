def checkRecord(s):
    ab = s.count('A')
    la = s.count('LLL')
    if ab > 1 or la >= 1:
        return False
    return True


a = "PPAALLL"
print(checkRecord(a))
