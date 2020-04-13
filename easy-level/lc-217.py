#  Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # also accepted solution but bit slower
        # from collections import Counter
        # c = Counter(nums)
        # for n in c.values():
        #     if n != 1:
        #         return True
        # return False

        # way faster!
        return len(nums) != len(set(nums))
