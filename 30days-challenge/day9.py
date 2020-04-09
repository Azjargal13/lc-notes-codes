# 844. Backspace String Compare

# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        from collections import deque
        s_stack = deque()
        for i in S:
            if i != '#':
                s_stack.append(i)
            elif len(s_stack) != 0:
                s_stack.pop()
        t_stack = deque()
        for i in T:
            if i != '#':
                t_stack.append(i)
            elif len(t_stack) != 0:
                t_stack.pop()
        while(len(s_stack) != 0):
            cur = s_stack.pop()
            if len(t_stack) == 0 or t_stack.pop() != cur:
                return False
        return len(s_stack) == 0 and len(t_stack) == 0


S = "ab#c"
T = "ad#c"
s = Solution()
print(s.backspaceCompare(S, T))
