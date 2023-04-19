import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class priority_queue_min:

    def __init__(self):
        self.heap = []
        self.h_size = -1

    def swap(self, ind1: int, ind2: int) -> None:
        self.heap[ind1], self.heap[ind2] = self.heap[ind2], self.heap[ind1]

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def get_left_child(self, index: int) -> int:
        return index * 2 + 1

    def get_right_child(self, index: int) -> int:
        return index * 2 + 2

    def shift_up(self, index: int) -> None:
        while index > 0 and self.heap[self.parent(index)][1] > self.heap[index][1]:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    def shift_down(self, index: int) -> None:
        min_ind = index
        # print(min_ind)
        left = self.get_left_child(index)
        if left <= self.h_size and self.heap[left][1] <= self.heap[min_ind][1]:
            min_ind = left

        right = self.get_right_child(index)
        if right <= self.h_size and self.heap[right][1] <= self.heap[min_ind][1]:
            min_ind = right

        if index != min_ind:
            self.swap(index, min_ind)
            self.shift_down(min_ind)

    def insert(self, priority: int, value: object) -> None:
        self.h_size += 1
        self.heap.append((priority, value))
        self.shift_up(self.h_size)

    def extract_min(self) -> int:
        min_el = self.heap[0]
        self.swap(0, self.h_size)
        self.h_size -= 1
        self.shift_down(0)
        self.heap = self.heap[:-1]
        return min_el

    def peek_min(self) -> int:
        return self.heap[0]

    def change_priority(self, index: int, priority: int) -> None:
        old_priority = self.heap[index][0]
        self.heap[index][0] = priority

        if priority < old_priority:
            self.shift_up(index)
        else:
            self.shift_down(index)

    def remove_elem(self, index: int) -> None:
        self.heap[index] = (self.peek_min() + 1, self.heap[index][1])

    def printer(self) -> None:
        print(self.heap)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        heap = priority_queue_min()
        for i in range(len(lists)):
            if lists[i]:
                heap.insert(i, lists[i].val)

        result = ListNode()
        end = result
        while heap.h_size > -1:
            i, val = heap.extract_min()
            end.next = ListNode(val)
            end = end.next
            lists[i] = lists[i].next
            if lists[i]:
                heap.insert(i, lists[i].val)

        return result.next
