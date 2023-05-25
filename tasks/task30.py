from typing import List
from collections import defaultdict


class Solution:

    def __task_init__(self, n, m, groups, predecessors):
        self.items_amount = n
        self.groups_amount = m
        self.groups = groups
        self.pred = predecessors

    def add_items_to_groups(self):
        for gr_item in range(len(self.groups)):
            if self.groups[gr_item] == -1:
                self.groups[gr_item] = self.groups_amount
                self.groups_amount += 1

    def build_graphs(self):
        self.graph_of_items = [[] for _ in range(self.items_amount)]
        self.outputs_of_items = [0] * self.items_amount
        self.graph_of_groups = [[] for _ in range(self.groups_amount)]
        self.outputs_of_groups = [0] * self.groups_amount

        for cur_item in range(self.items_amount):
            for start_item in self.pred[cur_item]:
                self.graph_of_items[start_item].append(cur_item)
                self.outputs_of_items[cur_item] += 1
                # but if items are not in the same group
                if self.groups[cur_item] != self.groups[start_item]:
                    # add connection btw group of start_item and group of cur_item (unite 2 gr)
                    self.graph_of_groups[self.groups[start_item]].append(self.groups[cur_item])
                    self.outputs_of_groups[self.groups[cur_item]] += 1

    def topological_sort(self, graph, outputs):
        target = len(graph)
        topo_order = []
        stack = [node for node in range(target) if outputs[node] == 0]
        while stack:
            start_node = stack.pop()
            topo_order.append(start_node)
            for cur_node in graph[start_node]:
                # break that connection
                outputs[cur_node] -= 1
                # if there is no output nodes of cur_node
                if outputs[cur_node] == 0:
                    stack.append(cur_node)
        return topo_order if len(topo_order) == target else []

    def toposort_for_groups(self):
        self.group_sorted = self.topological_sort(self.graph_of_groups, self.outputs_of_groups)
        if len(self.group_sorted) == 0:
            return False
        return True

    def toposort_for_items(self):
        self.item_sorted = self.topological_sort(self.graph_of_items, self.outputs_of_items)
        if len(self.item_sorted) == 0:
            return False
        return True

    def add_items_to_Megagroup(self):
        self.Megagroup = defaultdict(list)
        for cur_item in self.item_sorted:
            self.Megagroup[self.groups[cur_item]].append(cur_item)

    def combine_sorted_groups(self):
        self.ordered_groups = []
        for group in self.group_sorted:
            self.ordered_groups += self.Megagroup[group]

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        self.__task_init__(n, m, group, beforeItems)
        self.add_items_to_groups()
        self.build_graphs()
        if not self.toposort_for_groups() or not self.toposort_for_items():
            return []
        self.add_items_to_Megagroup()
        self.combine_sorted_groups()
        return self.ordered_groups
