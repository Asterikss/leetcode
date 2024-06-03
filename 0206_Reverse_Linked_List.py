from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        if head is None:
            return None

        next = head.next
        head.next = None
        prev = head

        while next:
            new_next = next.next
            next.next = prev
            prev = next
            next = new_next

        # print(prev)
        return prev


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp_curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_curr_next
        return prev


class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head
