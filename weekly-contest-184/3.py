# 5382. HTML Entity Parser
class Solution:
    def entityParser(self, text: str) -> str:

        text = text.replace('&quot;', '"')
        text = text.replace('&apos;', "'")
        text = text.replace("&amp;", "&")
        text = text.replace("&gt;", ">")
        text = text.replace("&lt;", "<")
        text = text.replace("&frasl;", "/")

        return text


text = "leetcode.com&frasl;problemset&frasl;all"
s = Solution()
print(s.entityParser(text))
