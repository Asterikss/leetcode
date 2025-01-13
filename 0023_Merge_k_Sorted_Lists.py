from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(nlogk) O(1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def mergeTwoLists(l1, l2):
            head = ListNode(-1)
            tail = head

            while l1 and l2:
                if l1.value <= l2.value:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2

            return tail.next

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+2) < len(lists) else None
                mergedLists.append(mergeTwoLists(l1, l2))
            lists = mergedLists

        return lists[0]


    # O(nk) O(1) are simmilar, but twice much faster. Still not as fast as it can be
    # since pairs are not used
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(list1, list2):
            original_fake_head = ListNode(0)
            fake_head = original_fake_head
            while list1 and list2:
                if list1.val <= list2.val:
                    fake_head.next = list1
                    fake_head = fake_head.next
                    list1 = list1.next
                else:
                    fake_head.next = list2
                    fake_head = fake_head.next
                    list2 = list2.next
            if list1:
                fake_head.next = list1
            elif list2:
                fake_head.next = list2

            return original_fake_head.next

        head = lists[0]
        for i in range(1, len(lists)):
            head = mergeTwoLists(lists[i], head)
        return head

    # O(nk) O(1)
    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        original_head = ListNode(-1)
        new_head = original_head

        smallest, smallest_idx = float("inf"), -1
        while True:
            for i, head in enumerate(lists):
                if head and head.val < smallest:
                    smallest = head.val
                    smallest_idx = i
            if smallest_idx == -1:
                return original_head.next
            new_head.next = lists[smallest_idx] # type: ignore
            new_head = new_head.next # type: ignore
            lists[smallest_idx] = lists[smallest_idx].next # type: ignore
            smallest, smallest_idx = float("inf"), -1
