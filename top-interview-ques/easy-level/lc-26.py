# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ind = 1
        n = len(nums)
        for i in range(n-1):
            print(i, nums[i], nums[i+1])
            if nums[i] != nums[i+1]:
                nums[ind] = nums[i+1]
                ind += 1
        return ind

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))