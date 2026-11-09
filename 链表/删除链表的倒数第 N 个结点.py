# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next

        target = len - n
        dummy = ListNode(0,head)
        cur = dummy

        for i in range(len-n):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next