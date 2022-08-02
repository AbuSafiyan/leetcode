def addBinary(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    add = int(num1, 2) + int(num2, 2)  # int(num1, 2) returns a decimal integer equivalent of binary number stored in num.
                                       # Here 2 is the base of number stored in num
    add = bin(add)      # bin() it will convert decimal to binary
    return add[2:]         # here we do slicing


print(addBinary(101, 111))
