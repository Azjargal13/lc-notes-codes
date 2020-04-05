# first task

# https: // leetcode.com/contest/weekly-contest-183/problems/minimum-subsequence-in-non-increasing-order/


def minSubsequence(nums: [int]) -> [int]:
    if len(nums) == 1:
        return nums
    else:
        nums.sort(reverse=True)
        s = sum(nums)
        res = []
        print(nums, s)
        for i in nums:
            # print(i)
            if s < sum(res):
                break
            s -= i
            print(s)
            res.append(i)
        return res


print(minSubsequence(nums=[4, 3, 10, 9, 8]))
