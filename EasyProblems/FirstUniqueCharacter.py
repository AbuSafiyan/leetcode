def firstUniqChar(s):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)

    return -1


a = "loveleetcode"
print(firstUniqChar(a))
