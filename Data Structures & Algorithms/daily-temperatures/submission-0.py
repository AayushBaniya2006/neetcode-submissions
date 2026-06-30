class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a stack, hold val, if greater remove 
        stack = []
        stackPos = []

        returnVar = [0] * len(temperatures) 

        for i in range(0,len(temperatures)):
            if(len(stack) == 0):
                stack.append(temperatures[i])
                stackPos.append(i)
            while(len(stack) > 0 and temperatures[i] > stack[-1]):
                print(returnVar[i - stackPos[-1]])
                returnVar[stackPos.pop()] = i - stackPos[-1]
                stack.pop()
            stack.append(temperatures[i])
            stackPos.append(i)


        return returnVar 