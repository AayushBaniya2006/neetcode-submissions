class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        distance = []
        ret = [0] * len(temperatures)
    
        for i in range(len(temperatures)):
            count = 1
            while stack and stack[-1] < temperatures[i]:
                stack.pop()
                temp = distance.pop()
                ret[temp] = i - temp
                count += 1;
            stack.append(temperatures[i])
            distance.append(i)
        
        

        return ret