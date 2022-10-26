# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

def addStrings(num1, num2):
    num3 = int(num1)
    num4 = int(num2)
    sum = num3 + num4
    return str(sum)


a = '12'
b = '112'
print(addStrings(a, b))

