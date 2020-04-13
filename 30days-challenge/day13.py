#  Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total = 0
        d = {0: 0}
        mx = 0
        if len(nums) <= 1:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    total -= 1

                else:
                    total += 1

                if total in d:
                    mx = max(mx, i+1-d[total])
                else:
                    d[total] = i+1
            return mx
