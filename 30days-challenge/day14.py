#  Perform String Shifts


class Solution:
    def stringShift(self, s: str, shift: [[int]]) -> str:
        for i in shift:
            if i[0] == 0:
                # shift left
                # left first half
                lh = s[0:i[1]]
                # left other half
                la = s[i[1]:]
                s = la+lh

                #print(s, lh, la)
            elif i[0] == 1:
                # print(s)
                # shift right
                # right first half
                rh = s[0:len(s)-i[1]]
                # right rest half
                ra = s[len(s)-i[1]:]
                s = ra+rh
        return s


ss = Solution()
s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]

print(ss.stringShift(s, shift))
