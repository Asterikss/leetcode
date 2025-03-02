from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  # O(N) and O(1) space. The second one is more interesting ey
  def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
    if not head.next:
      return None

    slow_pointer = head
    fast_pointer = head
    for _ in range(n):
      fast_pointer = fast_pointer.next  # type: ignore

    if fast_pointer is None:
      return head.next

    while fast_pointer.next:
      fast_pointer = fast_pointer.next
      slow_pointer = slow_pointer.next  # type: ignore

    slow_pointer.next = slow_pointer.next.next  # type: ignore

    return head

  # O(N) time, O(N) sapce, an array of length n+1; frist submit
  def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
    help_array = [None for _ in range(n + 1)]
    arr_len = len(help_array)
    curr = head
    index_counter = -1

    # [1,2,3,4]
    # n = 2
    # [4,2,3]
    while curr:
      index_counter += 1
      index_counter %= arr_len
      help_array[index_counter] = curr  # type: ignore
      curr = curr.next

    # [1, 2, NULL]
    # [4,2,3]
    #    |
    # Find node before (index) (can be None if the element to be removed is the first element)
    for _ in range(n):
      index_counter -= 1
      if index_counter < 0:
        index_counter = n

    if help_array[index_counter] is None:
      return head.next  # remove head # type: ignore

    if n == 1:  # The list cannot contain None at this point
      help_array[index_counter].next = None  # type: ignore
      return head

    # [4,2,3]
    # Find one after (index)
    new_next_index_counter = index_counter
    for _ in range(2):
      tmp_counter = new_next_index_counter + 1
      if tmp_counter > n:
        tmp_counter = 0
      # if help_array[tmp_counter]: # remove check
      new_next_index_counter = tmp_counter

    help_array[index_counter].next = help_array[new_next_index_counter]  # type: ignore

    return head
