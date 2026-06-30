class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #easiest way is O(n^2) - nested for loops

        duplicateHolder = set();

        for i in nums:
            if(i in duplicateHolder):
                return True;
            
            duplicateHolder.add(i)

        return False;

