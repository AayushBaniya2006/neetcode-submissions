class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        r = len(prices) - 1 
        maxs = prices[r]
        ret = 0
        for l in range(len(prices) - 1, -1, -1):
            if prices[l] < prices[r]:    
                ret += prices[r] - prices[l]
            r = l 
        return ret
        