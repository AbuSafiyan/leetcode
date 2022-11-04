# Given a string s,
# reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.


def reverseWords(s):
    return ' '.join(word[::-1] for word in s.split())


a = "Let's take LeetCode contest"
print(reverseWords(a))
