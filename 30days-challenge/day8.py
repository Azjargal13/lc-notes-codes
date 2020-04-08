# Middle of the Linked List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr1 = ptr2 = head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return ptr1
