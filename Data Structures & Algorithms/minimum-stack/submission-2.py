class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            topVal, topMin = self.stack[-1]
            newMin = min(topMin, val)
            self.stack.append((val, newMin))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            topVal, _ = self.stack[-1]
            return topVal
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            _, topMin = self.stack[-1]
            return topMin
        else:
            return None