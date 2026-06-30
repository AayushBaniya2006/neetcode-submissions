class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3, 4, 5, 0, 1, 2

        # 2, 1

        l, r = 0 , len(nums) - 1
        ret = nums[0]

        while(l <= r):

            mid = (l + r) // 2

            print(l)
            print(mid)
            print(r) 

            print("-")


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




        # 3, 4, 5, 6

        # 1, 2
        