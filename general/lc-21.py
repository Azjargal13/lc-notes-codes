# 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        track = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return track.next


c = Solution()
print(c.mergeTwoLists([1, 2, 4],
                      [1, 3, 4]))
