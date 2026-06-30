class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        returnVar = 0

        while(r < len(prices)):
            returnVar = max(prices[r]-prices[l], returnVar)
            if(prices[r] <= prices[l]):
                l = r
            
            r+=1
        


        return returnVar;