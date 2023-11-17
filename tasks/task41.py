import random
import sys


class ImplicitTreapNode:

    def __init__(self, value, priority, left=None, right=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.size = 1
        self.sum = value


class ImplicitTreap:

    def __init__(self):

        self.random_priorities = set()
        self.root = None

    def update_size(self, treap: ImplicitTreapNode) -> None:

        if treap == None:
            return
        treap.size = 1 + self.get_size(treap.left) + self.get_size(treap.right)

    def update_sum(self, treap: ImplicitTreapNode) -> None:

        if treap == None:
            return
        treap.sum = treap.value + self.get_sum(treap.left) + self.get_sum(treap.right)

    def get_size(self, treap: ImplicitTreapNode) -> int:

        if treap == None:
            return 0
        return treap.size

    def get_sum(self, treap: ImplicitTreapNode) -> int:

        if treap == None:
            return 0
        return treap.sum

    def get_random_priority(self) -> int:
        rand = random.randint(1, sys.maxsize)
        while (rand in self.random_priorities):
            rand = random.randint(1, sys.maxsize)
        self.random_priorities.add(rand)
        return rand

    def insert(self, index: int, value: object, priority=None) -> None:
        if priority != None:
            node = ImplicitTreapNode(value, priority)
        else:
            node = ImplicitTreapNode(value, self.get_random_priority())
        treap1, treap2 = self.split_by_size(self.root, index)
        self.root = self.merge(self.merge(treap1, node), treap2)

    def erase(self, index: int) -> None:
        L, R = self.split_by_size(self.root, index)
        removed, RR = self.split_by_size(R, 1)
        self.root = self.merge(self.root, RR)

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
            print(node.value, node.priority)
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
