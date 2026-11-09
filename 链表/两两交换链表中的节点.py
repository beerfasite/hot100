# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        dummy = ListNode(0,head)
        pre = dummy

        while pre.next and pre.next.next:
            first = pre.next
            second = first.next

            #swap
            first.next = second.next
            pre.next = second
            second.next = first

            pre = pre.next.next

        return dummy.next