# Best time to buy and sell stock II

# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/


def maxProfit(prices: [int]) -> int:
    A_ = sorted(prices, reverse=True)
    A = sorted(prices)
    if prices == A_:
        return 0
    if prices == A:
        return max(prices) - min(prices)
    else:
        buy = 0
        profit = []
        for i in range(1, len(prices)):
            #print(i, buy)
            if prices[i] > prices[buy]:
                profit.append(prices[i]-prices[buy])
            buy = i
        return sum(profit)


print(maxProfit([7, 1, 5, 3, 6, 4]))
#print(maxProfit([1, 2, 3, 4, 5]))
