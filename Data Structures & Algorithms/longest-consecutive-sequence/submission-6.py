class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        holder = set()
        for i in nums:
            holder.add(i)
        maxCount = 0 
        count = 0
        for i in holder:
            while i + 1 in holder: 
                count += 1 
                i = i + 1
            maxCount = max(maxCount, count)
            count = 0
        return maxCount + 1
