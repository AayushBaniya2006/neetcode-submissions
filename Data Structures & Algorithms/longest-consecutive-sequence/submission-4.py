class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}

        for num in nums:
            if(num-1 not in nums):
                hashset[num] = 1
        returnVar = 0;
        count = 0
        print(hashset)
        for num in hashset:
            x = num
            while x in nums:
                x = x+1;
                count+=1

            if(count>returnVar):
                print(num)
                returnVar = count
            count = 0

        return returnVar
