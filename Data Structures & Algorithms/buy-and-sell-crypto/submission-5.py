class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ret = 0 
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                ret = max(prices[i] - prices[l], ret)
        return ret 