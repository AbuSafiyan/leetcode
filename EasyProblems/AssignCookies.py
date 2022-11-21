# Assign Cookies
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

def findContentChildren(g, s):
    child = 0
    cookie = 0
    g.sort()
    s.sort()
    while child != len(g) and cookie != len(s):
        if s[cookie] >= g[child]:
            child += 1
            cookie += 1
        else:
            cookie += 1
    return child


g = [1, 2, 3, 4]
s = [1, 2, 3]
print(findContentChildren(g, s))
