def findTheDifference(s, t):

    for i in t:
        if s.count(i) != t.count(i):
            return i


a = ""
b = "y"
print(findTheDifference(a, b))
