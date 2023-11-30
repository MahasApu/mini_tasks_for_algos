class Union_Find():
    def __init__(self, amount: int):
        self.amount_eq_classes = amount
        self.rank = [0] * amount
        self.eq_class_inst = [i for i in range(amount)]
        self.left_items = [i for i in range(amount)]

    def find(self, inst: int) -> int:
        if self.eq_class_inst[inst] != inst:
            self.eq_class_inst[inst] = self.find(self.eq_class_inst[inst])
        return self.eq_class_inst[inst]

    def union(self, node1, node2):
        node1_inst = self.find(node1)
        node2_inst = self.find(node2)
        if node1_inst == node2_inst:
            return
        if self.rank[node1_inst] > self.rank[node2_inst]:
            self.eq_class_inst[node1_inst] = node2_inst
        else:
            self.eq_class_inst[node2_inst] = node1_inst
            if self.rank[node1_inst] == self.rank[node2_inst]:
                self.rank[node1_inst] += 1


def greedy_algo(data: list):
    data = sorted(data, key=lambda i: i[2], reverse=True)
    possible_time_table = []
    sum_fines = 0
    for index, task in enumerate(data):
        name, deadline, fine = task[0], task[1], task[2]
        possible_time_table.append(name)
        if index > deadline - 1:
            sum_fines += fine

    return possible_time_table, sum_fines


def Union_find_algo(data: list):
    """

    :param data: List[name, deadline, fine]
    :return: List[names], sum of fines
    """

    data = sorted(data, key=lambda i: i[2], reverse=True)
    eq_classes = len(data)
    union_find = Union_Find(eq_classes + 1)
    possible_time_table = [""] * eq_classes
    sum_fines = 0

    for task in data:
        task_name, deadline, fine = task
        class_eq = union_find.find(deadline)
        place_to_put = union_find.left_items[class_eq]

        if place_to_put <= 0:
            class_eq = union_find.find(eq_classes)
            place_to_put = union_find.left_items[class_eq]
            sum_fines += fine

        possible_time_table[place_to_put - 1] = task_name
        new_left = min(place_to_put, union_find.left_items[union_find.find(place_to_put - 1)])
        union_find.union(place_to_put, place_to_put - 1)
        union_find.left_items[union_find.find(place_to_put)] = new_left

    print(possible_time_table, sum_fines)
    return possible_time_table, sum_fines


def main():
    test_data = [['A', 3, 25], ['B', 4, 10], ['C', 1, 30], ['D', 3, 50], ['E', 3, 20]]
    print(greedy_algo(test_data))
    print(Union_find_algo(test_data))
