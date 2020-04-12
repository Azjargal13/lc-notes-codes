# 1408. String Matching in an Array


class Solution:
    def stringMatching(self, words: [str]) -> [str]:
        ans = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i != j:
                    if x in y:
                        ans.append(x)
                        break
        return ans


s = Solution()
words = ["blue", "green", "bu"]

print(s.stringMatching(words))
