from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        llist = ListNode()
        tail = llist

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return llist.next


class Solution2:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        first = list1
        second = list2

        if first.val <= second.val:
            new_list = ListNode(list1.val)
            first = first.next
        else:
            new_list = ListNode(list2.val)
            second = second.next

        new_list_head = new_list

        while True:
            if first is None and second is None:
                break
            if first is None:
                while second:
                    new_list.next = second
                    second = second.next
                    new_list = new_list.next
                break
            if second is None:
                while first:
                    new_list.next = first
                    first = first.next
                    new_list = new_list.next
                break

            if first.val <= second.val:
                new_list.next = first
                first = first.next
            else:
                new_list.next = second
                second = second.next

            new_list = new_list.next

        return new_list_head
