# wiggle sort 2

#  324. Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/


def wiggleSort(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    half = len(nums[::2])
    # even index
    # odd index
    #print(nums, nums[::2], nums[1::2], nums[:half][::-1], nums[half:][::-1])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


n = [1, 5, 1, 1, 6, 4]
print(wiggleSort(nums=n))
