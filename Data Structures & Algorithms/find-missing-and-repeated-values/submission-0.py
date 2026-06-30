class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        temp = set()
        ret = [0] * 2
        length = len(grid) * len(grid[0])
        
        for i in grid: 
            for x in i:
                if(x in temp):
                    ret[0] = x
                temp.add(x)

        for i in range(1, length + 1):
            if i not in temp:
                ret[1] = i
        return ret