# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group,
# which could be shorter than k but still must contain at least one character.
# Furthermore, there must be a dash inserted between two groups,
# and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.


def licenseKeyFormatting(s, k):
    s = s.upper().replace('-', '')
    result = []
    count = 0

    for i in reversed(range(len(s))):
        result.append(s[i])
        count += 1

        if count == k and i != 0:
            result.append("-")
            count = 0

    return ''.join(result[::-1])


a = "5F3Z-2e-9-w"
b = 4
print(licenseKeyFormatting(a, b))
