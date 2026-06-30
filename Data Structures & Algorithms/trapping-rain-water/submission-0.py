class Solution:
    def trap(self, height: List[int]) -> int:

        if(not height):
            return 0

        l,r = 0, len(height) -1 
        leftMax, rightMax = height[l], height[r]
        returnVar = 0
        while l < r: 
            if(leftMax < rightMax):
                l+=1
                leftMax = max(height[l], leftMax)
                returnVar +=  leftMax - height[l] 
            else: 
                r-=1
                rightMax = max(height[r], rightMax)
                returnVar +=  rightMax - height[r] 


        return returnVar