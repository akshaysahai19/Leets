class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    temp = 4
                    for (rr,rc) in [(-1,0),(1,0), (0,1),(0,-1)]:
                        r,c = i+rr, j+rc
                        if r>=0 and r<m and c>=0 and c<n:
                            if grid[r][c]==1:
                                temp-=1
                    ans+=temp
        
        return ans
                                
                        
                        