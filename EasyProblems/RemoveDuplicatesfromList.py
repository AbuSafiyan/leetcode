def removeduplicate(n):
    d = {}
    for i in n:
        d[i] = n.count(i)
    print(d)
    return list(d)


a = [1, 2, 3, 4, 3, 5, 4]
print(removeduplicate(a))
