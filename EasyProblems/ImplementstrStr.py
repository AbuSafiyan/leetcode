def str(a, b):
    if len(b) == 0:
        return 0
    for i in range(len(a)):
        if a[i:i + len(b)] == b:
            return True
    return False


print(str('hello', 'll'))
