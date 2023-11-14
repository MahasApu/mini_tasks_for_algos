import random
import sys
from random import randrange


class ImplicitTreapNode:

    def __init__(self, val, priority, left=None, right=None):
        self.val = val
        self.priority = priority
        self.left = left
        self.right = right
        self.size = 1
        self.sum = val


class ImplicitTreap:

    def __init__(self, array=None, rand=True):

        self.random_priorities = random.sample(range(100), len(array))
        self.root = None

        if array and rand:
            self.root = self.random_pull(array)
        elif array and not rand:
            self.root = self.determined_pull(array)

    def update_size(self, treap: ImplicitTreapNode):

        if treap == None:
            return
        treap.size = 1 + self.get_size(treap.left) + self.get_size(treap.right)

    def update_sum(self, treap: ImplicitTreapNode):

        if treap == None:
            return
        treap.sum = treap.val + self.get_sum(treap.left) + self.get_sum(treap.right)

    def get_size(self, treap: ImplicitTreapNode):

        if treap == None:
            return 0
        return treap.size

    def get_sum(self, treap: ImplicitTreapNode):

        if treap == None:
            return 0
        return treap.sum

    def determined_pull(self, array):

        treap = None
        for index, item in enumerate(array):
            value, priority = item
            node = ImplicitTreapNode(value, priority)
            treap = self.insert(treap, node, index)
        return treap

    def random_pull(self, array=None):

        treap = None
        for index, elem in enumerate(array):
            rand_index = randrange(len(self.random_priorities))
            rand_priority = self.random_priorities[rand_index]
            self.random_priorities.remove(rand_priority)

            node = ImplicitTreapNode(elem, rand_priority)
            treap = self.insert(treap, node, index)

        return treap

    def insert(self, treap: ImplicitTreapNode, node: ImplicitTreapNode, index: int):

        treap1, treap2 = self.split_by_size(treap, index)
        return self.merge(self.merge(treap1, node), treap2)

    def merge(self, treap1: ImplicitTreapNode, treap2: ImplicitTreapNode) -> ImplicitTreapNode:

        if treap1 == None: return treap2
        if treap2 == None: return treap1

        if treap1.priority < treap2.priority:
            treap1.right = self.merge(treap1.right, treap2)
            self.update_size(treap1)
            self.update_sum(treap1)
            return treap1
        else:
            treap2.left = self.merge(treap1, treap2.left)
            self.update_size(treap2)
            self.update_sum(treap2)
            return treap2

    def split_by_size(self, treap: ImplicitTreapNode, key: int) -> (ImplicitTreapNode, ImplicitTreapNode):

        if treap == None:
            return None, None

        left_size = self.get_size(treap.left)
        if key <= left_size:
            LL, LR = self.split_by_size(treap.left, key)
            treap.left = LR
            self.update_size(treap)
            self.update_sum(treap)
            return LL, treap
        else:
            RL, RR = self.split_by_size(treap.right, key - left_size - 1)
            treap.right = RL
            self.update_size(treap)
            self.update_sum(treap)
            return treap, RR

    def print_helper(self, node: ImplicitTreapNode, indent: str, last: bool) -> None:

        if node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(node.val, node.priority)
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)

    def sum(self, start: int, end: int) -> int:

        if start > self.root.size or end > self.root.size:
            raise IndexError("Index out of range! for Tasya")

        L, R = self.split_by_size(self.root, start)
        RL, RR = self.split_by_size(R, end - start + 1)
        result = self.get_sum(RL)
        self.root = self.merge(self.merge(L, RL), RR)
        return result
