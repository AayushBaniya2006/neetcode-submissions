class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        minVal = prices[l]
        returnVal = 0 
        while r < len(prices):
            if(prices[r] < minVal):
                minVal = prices[r]
                l = r 
            returnVal = max(returnVal, prices[r] - prices[l])
            r += 1

        return returnVal
            
