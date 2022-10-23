def isSubsequence(s, t):
    left = 0
    right = 0
    while left < len(s) and right < len(t):
        l1 = s[left]
        r1 = t[right]
        if s[left] == t[right]:
            left += 1
            right += 1
        else:
            right += 1
    if left == len(s):
        return True
    else:
        return False

        
a = "abc"
b = "ahbgdc"
print(isSubsequence(a, b))
