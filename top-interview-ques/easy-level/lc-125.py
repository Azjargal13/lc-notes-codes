# Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while (l < r):
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # or another smart solution
        s = s.lower()
        ss = [i for i in s if i.isalnum()]
        # ss = []
        # for i in s:
        #     if i.isalnum():
        #         ss.append(i)
        rev_ss = ss[::-1]
        if rev_ss == ss:
            return True
        return False

        #s = ''.join(e for e in s if e.isalnum()).lower()
        # return s==s[::-1]
