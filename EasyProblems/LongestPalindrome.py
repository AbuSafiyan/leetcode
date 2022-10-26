# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case-sensitive, for example, "Aa" is not considered a palindrome here.


def longestPalindrome(s):
    dic = {}
    res = 0
    odd = False

    for i in s:
        dic.update({i: s.count(i)})

    for key, value in dic.items():
        if value % 2 == 0:
            res += value
        else:
            res += value - 1
            odd = True

    if odd:
        return res + 1
    else:
        return res


a = "abccccdd"
print(longestPalindrome(a))
