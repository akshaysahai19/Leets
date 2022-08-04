class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp = {}
        
        def findPath(m,n):
            
            if (m,n) in dp:
                return dp[(m,n)]
            
            
            if m<0 or m>=len(obstacleGrid) or n<0 or n>=len(obstacleGrid[0]):
                return 0
            
            if obstacleGrid[m][n]==1:
                return 0
            
            if m==len(obstacleGrid)-1 and n==len(obstacleGrid[0])-1:
                return 1
            
            dp[(m,n)] = findPath(m, n+1) + findPath(m+1, n)
            
            return dp[(m,n)]
        
        return findPath(0,0)
            
        