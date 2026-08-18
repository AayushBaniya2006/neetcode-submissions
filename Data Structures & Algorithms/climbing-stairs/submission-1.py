class Solution:
    def climbStairs(self, n: int) -> int:
        temp = {}
        return self.helper(n, temp)
    
    def helper(self,n, temp): 
        if n == 1:
            return 1
        if  n == 2:
            return 2
        if n in temp:
            return temp[n]
        else:
            temp[n] = self.helper(n-1, temp) + self.helper(n-2, temp)
        return temp[n]