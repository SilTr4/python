class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append((val, val))
        else:
            self.arr.append((val, min(val, self.arr[-1][1])))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]