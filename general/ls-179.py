# largest number

# 179. Largest Number
# https://leetcode.com/problems/largest-number/

import itertools


class Solution:
    def largestNumber(self, nums: [int]) -> str:
        s = ""

        for i in nums:
            s += str(i)
        res = nums

        lar = int(s)
        for i in range(len(s)):
            #print(i, len(s))
            if int(s[i]) < int(len(s)):
                print(res[i])
                res[i], res[i+1] = res[i+1], res[i]
                if int(res) > lar:
                    lar = int(res)
        return str(lar)


n = [10, 2]
s = Solution()
print(s.largestNumber(n))
