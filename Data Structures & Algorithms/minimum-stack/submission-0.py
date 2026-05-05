class MinStack:

    def __init__(self):
        self.minVal = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal:
            temp = self.minVal[-1]
            x = min(temp, val)
            self.minVal.append(x)
        else:
            self.minVal.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
