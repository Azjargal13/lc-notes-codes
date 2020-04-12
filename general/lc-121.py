# 121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mcur = 0
        mSoFar = 0
        # kadane's algo O(n)
        for i in range(1, len(prices)):
            mcur += prices[i] - prices[i-1]
            mcur = max(0, mcur)
            mSoFar = max(mcur, mSoFar)
        return mSoFar


s = Solution()
p = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(p))
