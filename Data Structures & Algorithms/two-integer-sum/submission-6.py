class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        holder = {}

        for i in range(len(nums)):
            if target - nums[i] in holder:
                return [holder[target - nums[i]], i]
            holder[nums[i]] = i
        

