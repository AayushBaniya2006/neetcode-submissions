class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3

        for i in nums:
            if i == 0:
                bucket[0] += 1 
            elif i == 1: 
                bucket[1] += 1
            else:
                bucket[2] += 1 
        pos = 0 
        for i in range(len(bucket)):
            for x in range(bucket[i]):
                nums[pos] = i
                pos += 1 
