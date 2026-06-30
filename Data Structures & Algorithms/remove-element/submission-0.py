class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #l point and r point, r will check if its not = to val, if it isnt we 
        #can then slot into left 

        l = 0

        for r in range(0, len(nums)):
            if(nums[r] != val):
                nums[l] = nums[r]
                l+=1
            

        return l