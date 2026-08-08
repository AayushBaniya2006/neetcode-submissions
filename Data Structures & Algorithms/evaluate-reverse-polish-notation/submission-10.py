class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        holder = 0
        for i in tokens:
            if i == "+": 
                holder = stack.pop()
                stack.append(holder + stack.pop())
            elif i == "-": 
                holder = stack.pop()
                stack.append(stack.pop() - holder)
            elif i == "*": 
                holder = stack.pop()
                stack.append(holder * stack.pop())
            elif i == "/": 
                holder = stack.pop()
                stack.append(int(stack.pop() / holder))
            else: 
                stack.append(int(i))
        return stack.pop()