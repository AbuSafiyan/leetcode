# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j]
# then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.


def findRestaurant(list1, list2):

    d = {}
    for i in list1:
        if i in list2:
            val = list1.index(i) + list2.index(i)
            d[i] = val

    m = min(list(d.values()))
    res = []
    for key, val in d.items():
        if val <= m:
            m = val
            res.append(key)

    return res


a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
b = ["KFC", "Shogun", "Burger King"]
print(findRestaurant(a, b))
