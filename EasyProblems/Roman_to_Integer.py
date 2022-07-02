def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    curr = 0
    total = 0
    for i in range(len(s)):
        curr = d[s[i]]
        if curr > prev:
            total = total + curr - 2 * prev
        else:
            total = total + curr
        prev = curr
    return total


a = 'V'
print(romanToInt(a))