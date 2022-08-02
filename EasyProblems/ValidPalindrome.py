def isPalindrome(s):
    b = s.lower()
    res = ""
    res1 = ""
    if s == " ":
        return True
    else:
        for i in b:
            if i.isalnum():
                res += i
        print(res)
        for i in b:
            if i.isalnum():
                res1 = i + res1
        print(res1)
        if res == res1:
            return True
        else:
            return False


a = 'Abu Safiyan'
print(isPalindrome(a))
