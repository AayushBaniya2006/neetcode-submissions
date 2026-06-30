class MinStack:
    stack = []
    stackmin = []
    
    def __init__(self):
        self.stackmin = [sys.maxsize]
        self.stack = []
        

    def push(self, val: int) -> None:
        temp = self.stackmin[-1]
        if val <= temp:
            self.stackmin.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.stackmin[-1]:
            self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]