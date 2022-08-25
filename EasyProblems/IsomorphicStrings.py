# IsomorphicStrings.py


"""1- Consider a mapping table that maps each char from the first string to one and only char in the second string.
2- Consider a mappedBefore table that record each char from the second string that is already related to a char
   from the first string.
3- Read characters of the first string one by one.
4- If the read char from the first string is in the mapping table get its mapping.
5- Read the related char from the second string.
6- If the mapping and the read char from the second string are not the same return false.
7- Else If the read char from the first string does not exist in the mapping table,
	 *    1- read the related char from the second string,
	 *    2- If the char exist in the mappedBefore table, return false.
	 *    3- Else, add the read char from the first table and the read char from the second table to the
	      mapping table.
8- Go to 3- and continue.
9 - Return true."""


def isIsomorphic(s, t):
    map1 = {}
    map2 = {}
    if len(s) != len(t):
        return False

    for c1, c2 in zip(s, t):
        if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
            return False
        map1[c1] = c2
        map2[c2] = c1
    return True


print(isIsomorphic('paper', 'title'))
