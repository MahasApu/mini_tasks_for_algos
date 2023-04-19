class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val:
            self.min_val.append(val)
        else:
            if val <= self.min_val[-1]:
                self.min_val.append(val)

    def pop(self) -> None:
        if self.stack:
            a = self.stack.pop()
        if self.min_val[-1] == a:
            self.min_val.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_val:
            return self.min_val[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()