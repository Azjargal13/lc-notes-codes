# 191. Number of 1 Bits

# hamming weight


class Solution:
    def hammingWeight(self, n: int) -> int:
        # simple built in
        # s = str(n).count('1')
        # print(s)

        # bit operation
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c


n = int("00000000000000000000000000001011")
s = Solution()
print(s.hammingWeight(n))
