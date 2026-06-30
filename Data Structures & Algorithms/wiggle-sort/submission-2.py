class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        x = 1
        for i in range(1, len(nums), 2):
            nums[i] = temp[len(nums) - x]
            x+=1

        x = 0
        for i in range(0, len(nums), 2):
            nums[i] = temp[x]
            x+=1


        