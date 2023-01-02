class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        paths = []
        dp = {}
        
        def countPaths(x,y, curr):
            
            if (x,y) in dp:
                return dp[(x,y)]
            
            if x==m-1 and y==n-1:
                return 1
            
            if x<0 or y<0 or x>=m or y>=n:
                return 0
            
            dp[(x,y)] = countPaths(x,y+1, curr+[(x,y)]) + countPaths(x+1,y, curr+[(x,y)])
            
            return dp[(x,y)]
        
        return countPaths(0,0, [])
        
