from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reorderList(self, head: ListNode) -> None:
    # little cleaner better finding the head of the second list (middle)
    slow, fast = head, head.next
    while fast and fast.next:
      slow = slow.next  # type: ignore
      fast = fast.next.next

    second = slow.next  # type: ignore # Does not need to be .next here
    slow.next = None  # type: ignore

    # Revrse the second list
    prev = None
    while second:
      tmp = second.next
      second.next = prev
      prev = second
      second = tmp

    # Merge both halfes
    first, second = head, prev  # new head of the second half of the list
    while second:  # we know that only the second list might be longer since the second = slow.next line choice
      tmp1, tmp2 = first.next, second.next  # type: ignore
      first.next = second  # type: ignore
      second.next = tmp1
      first = tmp1
      second = tmp2

  # In place, but unnecessary reversal (lil help (mad))
  def reorderList2(self, head: ListNode) -> None:
    if not head.next:
      return

    # Find the middle
    slow = head
    fast = head
    middle = None

    # fast, slow and middle pointer here no pointer, but Objects
    while fast and fast.next:
      middle = slow
      slow = slow.next  # type: ignore
      fast = fast.next.next

    second_head = middle.next  # type: ignore
    middle.next = None  # type: ignore

    # curr=1 tbm=2 3
    # tmp=3
    # 2 -> 1 -> X
    # curr=2 tbm=3
    # 3 -> 2 -> 1 -> X
    curr = second_head
    to_be_moved = second_head.next  # type: ignore
    second_head.next = None  # type: ignore
    while to_be_moved:
      tmp = to_be_moved.next
      to_be_moved.next = curr
      curr = to_be_moved
      to_be_moved = tmp

    # 1 2
    # 3 4
    # m=2 f=N s=N s=F
    # 1 -> 3 -> 2 -> 4 -> X
    master_head = head
    first_list_head = head.next
    second_list_head = curr
    switch = False
    while first_list_head and second_list_head:
      if switch:
        master_head.next = first_list_head
        first_list_head = first_list_head.next
      else:
        master_head.next = second_list_head
        second_list_head = second_list_head.next
      switch = not switch
      master_head = master_head.next

    # Handle remaining nodes in either list
    if first_list_head:
      master_head.next = first_list_head
    elif second_list_head:
      master_head.next = second_list_head

  # Not O(1) memory, but ok
  def reorderList3(self, head: Optional[ListNode]) -> None:
    nodes = []
    curr_node = head
    while curr_node:
      next_node = curr_node.next
      curr_node.next = None
      nodes.append(curr_node)
      curr_node = next_node

    # print(nodes)
    # []
    # [2,8,4,6]
    # 2 -> 8 -> 4 -> 6
    head = nodes.pop(0)
    from_front = False
    last_node = head
    while nodes:
      next_node = None
      if from_front:
        next_node = nodes.pop(0)
      else:
        next_node = nodes.pop()
      last_node.next = next_node  # type: ignore
      last_node = next_node
      from_front = not from_front
