class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        maxVal = 0
        currCount = 0 

        while r < len(nums):
            if nums[r] == 1:
                r+=1
                currCount+=1
            else: 
                print(r)
                maxVal = max(maxVal, currCount)
                l= r
                r+=1
                currCount = 0
        maxVal = max(maxVal, currCount)
        print(currCount)
        return maxVal
