# Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # kinda slow approach

        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)
        #         nums.append(0)
        # #nums.remove(0)
        # print(nums)

        # faster approach, swap elems
        swap = 0
        for i, val in enumerate(nums):
            if val != 0:
                nums[swap], nums[i] = nums[i], nums[swap]
                swap += 1
        print(nums)
