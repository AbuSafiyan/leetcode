# Given a string 's',return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non - space characters.


def countSegments(s):
    arr = s.split()
    return len(arr)


a = "Hello, my name is John"
print(countSegments(a))
