# Counting Elements
class Solution:
    def countElements(self, arr: [int]) -> int:
        s = arr[0]
        cnt = 0
        for i in range(1, len(arr)):
            if i+1 in arr:
                cnt += 1
        return cnt


s = Solution()
print(s.countElements([1, 2, 3]))
