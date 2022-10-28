def repeatedSubstringPattern(s):
    length = len(s)

    for i in range(length // 2, 0, -1):
        if length % i == 0:
            string = s[:i]
            times = length // i
            ns = ""
            for j in range(0, times):
                ns += string
            if ns == s:
                return True
    return False


a = "abab"
print(repeatedSubstringPattern(a))
