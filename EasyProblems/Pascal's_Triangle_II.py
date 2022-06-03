def getRow(rowIndex):
    result = []

    for i in range(0, rowIndex + 1):
        result.append([])

        for j in range(0, i + 1):
            if j == 0:
                result[i].append(1)
            elif i == j:
                result[i].append(1)
            else:
                result[i].append((result[i - 1][j - 1]) + (result[i - 1][j]))

    return result[rowIndex]


n = 6
print(getRow(n))