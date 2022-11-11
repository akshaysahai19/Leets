class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = []
        
        m = len(grid)
        n = len(grid[0])
        
        def findIslands(i,j, count):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            
            grid[i][j]=0
            a = findIslands(i-1,j, count+1)
            b = findIslands(i+1,j, count+1)
            c = findIslands(i,j-1, count+1)
            d = findIslands(i,j+1, count+1)
            
            return 1+a+b+c+d
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans.append(findIslands(i,j, 0))
        
        return 0 if not ans else max(ans)