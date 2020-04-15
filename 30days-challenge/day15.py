# Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        out = [1] * len(nums)
        pi = pj = 1
        for i, v in enumerate(nums):
            j = -1-i
            # print(j)
            out[i] *= pi
            out[j] *= pj
            pi *= nums[i]
            pj *= nums[j]
            # print(out)
        return out


s = Solution()
print(s.productExceptSelf([5, 1, 3, 10]))
