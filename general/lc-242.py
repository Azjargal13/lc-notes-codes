# 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c = Counter(s)
        c1 = Counter(t)
        return c == c1


s = Solution()
ss = "rat"
t = "car"
print(s.isAnagram(ss, t))
