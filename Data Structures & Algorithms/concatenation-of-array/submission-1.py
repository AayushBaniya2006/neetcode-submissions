class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        nums2 = [0] * (len(nums)*2)
        length = len(nums)

        for x in range(0, length):
            nums2[x] = nums[x]
            nums2[x+length] = nums[x]

        return nums2