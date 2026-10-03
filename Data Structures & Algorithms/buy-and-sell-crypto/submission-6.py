class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        ret = sys.maxsize

        for i in prices: 
            if i < ret: 
                ret = i 
            print(ret)
            temp = max(temp, i-ret)

        return temp
