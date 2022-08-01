def lengthOfLastWord(s):
    s1 = s.split()
    ss = []
    for a in s1:
        ss.append(a)
    return len(ss[-1])


print(lengthOfLastWord('hello word'))
