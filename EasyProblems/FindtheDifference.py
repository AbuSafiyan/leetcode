def findTheDifference(s, t):

    for i in t:
        if s.count(i) != t.count(i):
            return i


a = "abu"
b = "abcd"
print(findTheDifference(a, b))
