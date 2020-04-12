# 70. Climbing Stairs
# can be solved by DP or recursive


class Solution:
    def climbStairs(self, n: int) -> int:
        # too much time consuming (exponential)
        # def climbWays(n: int) -> int:
        #     if n <= 1:
        #         return n
        #     return climbWays(n-1)+climbWays(n-2)
        # return climbWays(n+1)
        # optimized solution O(n) with dp

        def climbWaysDP(n) -> int:
            if (n == 1):
                return 1
            first = 1
            second = 2
            for i in range(3, n+1):
                third = first + second
                first = second
                second = third
            return second

        return climbWaysDP(5)

        # result = []

        # result.append(0)
        # result.append(1)
        # result.append(2)

        # for i in range(3,n+1) :
        #     result.append(result[i-1] + result[i-2])

        # return result[n]


s = Solution()
print(s.climbStairs(4))
