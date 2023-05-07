from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.count_val = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.count_val[val] += 1
        if self.count_val[val] > self.max_count:
            self.max_count = self.count_val[val]
        self.stacks[self.count_val[val]].append(val)

    def pop(self) -> int:
        result = self.stacks[self.max_count].pop()
        self.count_val[result] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()