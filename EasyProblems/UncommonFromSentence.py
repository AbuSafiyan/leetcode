def uncommonFromSentences(s1, s2):
    s3 = s1.split()
    s4 = s2.split()
    s5 = []

    for i in s3:
        if i not in s4:
            if s3.count(i) == 1:
                s5.append(i)

    for i in s4:
        if i not in s3:
            if s4.count(i) == 1:
                s5.append(i)

    return s5


a = "this apple is sweet"
b = "this apple is sour"
print(uncommonFromSentences(a, b))