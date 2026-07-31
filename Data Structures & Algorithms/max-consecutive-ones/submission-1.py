class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        maxVal = 0

        while r < len(nums):
            if nums[r] == 1:
                r+=1
            else: 
                print(r)
                maxVal = max(maxVal, r-l)
                r+=1
                l= r
        maxVal = max(maxVal, r-l)
        return maxVal
