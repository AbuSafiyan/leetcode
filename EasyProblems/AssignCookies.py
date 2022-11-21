# Assign Cookies
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

def findContentChildren(g, s):
    i = 0
    j = 0
    g_len = len(g)
    s_len = len(s)
    g.sort()
    s.sort()
    while i != g_len and j != s_len:
        if s[j] >= g[i]:
            i += 1
            j += 1
        else:
            j += 1
    return i


g = [1, 3, 2]
s = [1, 2, 3]
print(findContentChildren(g, s))
