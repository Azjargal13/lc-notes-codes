# First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        cnt = 0
        for k, v in c.items():
            if v == 1:
                return s.index(k)
            else:
                cnt += v
        if cnt == len(s):
            return -1
