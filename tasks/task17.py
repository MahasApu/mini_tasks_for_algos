
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):

        if left == right:
            return head

        node = ListNode()
        node.next = head
        tmp = node

        for i in range(left - 1):
            tmp = tmp.next

        current = tmp.next
        for j in range(right - left):
            t = current.next
            current.next = t.next
            t.next = tmp.next
            tmp.next = t

        return node.next