class MinStack:

    def __init__(self):
        self.arr = []
        self.stack = []

    def push(self, val: int) -> None:
        self.arr.append(val);

        localMin = min(val, self.stack[-1] if self.stack else val)
        self.stack.append(localMin)

    def pop(self) -> None:
        self.arr.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.stack[-1]
