# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        """
        设头节点到入环口需要走 a 步。设环长为 c。
        设相遇的时候，慢指针走了 b 步，那么快指针走了 2b 步。
        设快指针比慢指针多走了 k 圈，即 (2b - b = kc)，得 (b = kc)。

        慢指针从入环口开始，在环中走了 (b - a = kc - a) 步到达相遇点。
        这说明从相遇点开始，再走 a 步，就恰好走到入环口了！
        虽然不知道 a 是多少，但如果让头节点和慢指针同时走，
        恰好 a 步后二者必定相遇，且相遇点就在入环口。
        """
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while slow != head:
                    """slow和head再继续走a步"""
                    slow = slow.next
                    head = head.next
                return slow
        
        return None