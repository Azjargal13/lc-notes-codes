# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        res = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            # print(i)
            else:
                return res
        return res


s = Solution()
print(s.longestCommonPrefix(["racedog", "racecar", "racar"]))
