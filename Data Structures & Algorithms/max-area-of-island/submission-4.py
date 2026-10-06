class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
          
        count = 0
        rows = len(grid)-1
        cols = len(grid[0])-1
        def dfs(r,c):
            
            if r < 0 or c < 0 or r > rows or c > cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 
           
            return (1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1))
        
        
        for i in range(len(grid)):
            for w in range(len(grid[0])):
                if grid[i][w] == 1:
                    count = max(count, dfs(i,w))

        return count
