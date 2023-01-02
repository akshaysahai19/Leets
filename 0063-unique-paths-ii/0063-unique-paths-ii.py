class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        res = []
        dp = {}
        
        def countPath(x,y):
            if (x,y) in dp:
                return dp[(x,y)]
            
            if x<0 or y<0 or x>=m or y>=n or obstacleGrid[x][y]==1:
                return 0
            
            if x==m-1 and y==n-1:
                return 1
            
            dp[(x,y)] = countPath(x+1, y)+countPath(x,y+1)
            
            return dp[(x,y)]
        
        return countPath(0,0)