# Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        C = collections.Counter
        return list((C(nums1) & C(nums2)).elements())
