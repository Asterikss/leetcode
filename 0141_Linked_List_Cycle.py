from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        
        return False

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        p1 = p2 = head
        while True:
            if p1.next is None:
                return False
            if p2.next is None or p2.next.next is None:
                return False
            
            
            p1 = p1.next
            p2 = p2.next.next
            
            if p1 == p2:
                return True

class Solution3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        all_nodes = set()
        while True:
            if head.next is None:
                return False
            if head in all_nodes:
                return True
            all_nodes.add(head)
            head = head.next


class Solution4:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # 1234234_
        # 4 1
        # 12342432_
        # 122_
        curr_node = head
        all_vals: str = ""
        while True:
            if curr_node.next is None:
                return False
            curr = str(curr_node.val)

            if (prev_index := all_vals.find(curr)) != -1:
                j = 0
                top_boundry = len(all_vals) - prev_index
                tmp_curr = curr_node
                while j < top_boundry:
                    if tmp_curr.next is None:
                        return False
                    tmp_curr = tmp_curr.next
                    if tmp_curr == curr_node:
                        return True
                    j += 1

            all_vals += curr

            curr_node = curr_node.next


class Solution5:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # 1234234_
        # 4 1
        # 12342432_
        # 122_
        curr_node = head
        all_vals: str = ""
        while True:
            if curr_node.next is None:
                return False
            if curr_node.next == curr_node:
                return True
            curr = str(curr_node.val)

            if curr in all_vals and all_vals.find(curr) != all_vals.rfind(curr):
                prev_curr_idx = all_vals.rfind(curr)
                prev_prev_curr_idx = all_vals[:prev_curr_idx].rfind(curr)
                cycle1 = all_vals[prev_prev_curr_idx:prev_curr_idx]
                cycle2 = all_vals[prev_curr_idx:]
                # print(cycle1, cycle2, all_vals)
                if len(cycle1) > 0 and cycle1 == cycle2:
                    j = 0
                    tmp_curr = curr_node
                    while j <= len(cycle1):
                        if tmp_curr.next is None:
                            return False
                        tmp_curr = tmp_curr.next
                        if tmp_curr == curr_node:
                            return True
                        j += 1

                    return True
            all_vals += curr

            curr_node = curr_node.next
