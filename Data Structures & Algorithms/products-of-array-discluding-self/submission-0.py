class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        rightSum = [0] * len(nums)
        leftSum = [0] * len(nums)

        leftSum[0] = nums[0]
        rightSum[len(nums)-1] = nums[len(nums)-1]
        sum = [0] * len(nums)

        #[0]

        if(len(nums) == 1):
            return [0];
        

        #leftsum =    1,  2, 8,48
        #rightsum =   48,48,24, 6
        for x in range(1, len(nums), 1):
            leftSum[x] = leftSum[x-1] * nums[x];
            print(leftSum[x])
       

        for x in range(len(nums)-2, -1, -1):
            rightSum[x] = rightSum[x+1] * nums[x];
            print(x)


        for x in range(0, len(nums), 1):
            if(x == 0):
                sum[x] = rightSum[x+1]
            
            elif(x == len(nums) -1):
                sum[x] = leftSum[x-1]
            
            else: 
                sum[x] = rightSum[x+1] * leftSum[x-1]
        return sum



