def maxProfit(prices):
    l, r = 0, 1
    max_Prof = 0
    while len(prices) > r:
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_Prof = max(max_Prof, profit)
        else:
            l = r
        r += 1
    return max_Prof


a = [7, 1, 3, 5, 6, 4]
print(maxProfit(a))
