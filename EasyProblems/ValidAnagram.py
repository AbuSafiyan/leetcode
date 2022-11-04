def isAnagram(s, t):
    if len(s) != len(t):
        return False

    elif sorted(s) == sorted(t):
        return True

    else:
        return False


print(isAnagram('baccbbbdabcdbca', 'abc'))
