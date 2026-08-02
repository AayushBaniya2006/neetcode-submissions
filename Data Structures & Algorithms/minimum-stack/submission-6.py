class MinStack:

    
    def __init__(self):
        self.minimum = sys.maxsize
        self.stack = []

    def push(self, val: int) -> None:
        if(val < self.minimum):
            self.minimum = val
        self.stack.append([val, self.minimum])


    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.minimum = self.stack[-1][1]
        else: 
            self.minimum = sys.maxsize
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minimum
        
        
