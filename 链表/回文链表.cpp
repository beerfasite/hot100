/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    ListNode* middlenode(ListNode* head)
    {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        return slow;

    }

    ListNode* reverseList(ListNode* head) {
        ListNode *cur = head;
        ListNode *pre = NULL;

        while(cur)
        {
            ListNode *nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }

        return pre;
    }


public:
    bool isPalindrome(ListNode* head) {
        ListNode* mid = middlenode(head);
        ListNode* head2 = reverseList(mid);
        while(head && head2)
        {
            if(head->val != head2->val)return false;

            head = head->next;
            head2 = head2->next;
        }

        return true;
    }
};