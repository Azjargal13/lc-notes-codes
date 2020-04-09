# 1. Two Sum
# https://leetcode.com/problems/two-sum/


def twoSum(nums: [int], target: int) -> [int]:
    # ret = []
    # nums.sort()
    # med = len(nums)//2
    # print(med, nums[med])
    # min_half, max_half = nums[:med], nums[med:]
    # print(min_half, max_half)
    # if nums[med] > target:  # search from min half
    #     for i in range(len(min_half)-1):
    #         if min_half[i] != min_half[i+1]:
    #             print(i, min_half[i])

    # else:
    #     for i in max_half:
    #         return []
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        print(m)
        if m in d:
            return [d[m], i]
        else:
            d[n] = i


nums = [2, 2, 7, 7, 11, 15]
target = 9

print(twoSum(nums, target))
