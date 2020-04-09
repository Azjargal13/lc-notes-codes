# 169. Majority Element

# Boyer-Moore Majority Vote Algorithm
# https://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        # majority elem appears more than n/2 times
        # linear time, O(1) space
        maj = nums[0]
        c = 1
        i = 1
        while i < len(nums):
            if c == 0:
                maj = nums[i]
                c += 1
            elif maj == nums[i]:
                c += 1
            else:
                c -= 1
            i += 1
        return maj

        # more quick solution
        # nums.sort()
        # return nums[len(nums)//2]


s = Solution()
n = [2, 2, 1, 1, 1, 2, 2]
print(s.majorityElement(n))
