def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    curr = strs[0]
    for i in range(len(strs)):
        temp = ''
        if len(curr) == 0:
            break
        for j in range(len(strs[i])):
            if j < len(curr) and curr[j] == strs[i][j]:
                temp += curr[j]
            else:
                break
        curr = temp
    return curr


a = ['flower', 'fly', 'flight']
print(longestCommonPrefix(a))
