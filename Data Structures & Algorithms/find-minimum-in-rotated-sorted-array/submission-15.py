class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        ret = nums[0]

        while(l <= r):
            mid = (l + r) // 2
            if(nums[mid] > nums[r]):
                l = mid + 1
            elif(nums[mid] < nums[l]):
                ret = nums[mid]
                r = mid - 1
            else:
                r = mid -1

        print(ret)
        ret = min(ret, nums[mid])
        return ret
        