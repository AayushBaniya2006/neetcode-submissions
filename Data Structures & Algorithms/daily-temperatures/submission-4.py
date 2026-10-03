class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                x = stack.pop()
                ret[x[1]] = i - x[1]
            stack.append([temperatures[i], i])
        return ret