class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        x = 1
        for i in range(1, len(nums), 2):
            nums[i] = temp[len(nums) - x]
            nums[i-1] = temp[x-1]
            x+=1


        