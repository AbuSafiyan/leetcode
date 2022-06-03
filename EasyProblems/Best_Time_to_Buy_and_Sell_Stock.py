def maxProfit(prices):
    left_Pointer, right_Pointer = 0, 1
    max_Profit = 0
    while len(prices) > right_Pointer:
        if prices[left_Pointer] < prices[right_Pointer]:
            profit = prices[right_Pointer] - prices[left_Pointer]
            max_Prof = max(max_Prof, profit)
        else:
            left = right_Pointer
        right_Pointer += 1
    return max_Profit


a = [7, 1, 3, 5, 6, 4]
print(maxProfit(a))
