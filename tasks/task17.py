from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        node_prev = None
        node = head

        for i in range(left - 1):
            node_prev = node
            node = node.next

        prev = node
        cur = node.next
        for j in range(right - left):
            cur.next, prev, cur = prev, cur, cur.next

        node.next = cur
        if node_prev:
            node_prev.next = prev
            prev = head

        return prev
