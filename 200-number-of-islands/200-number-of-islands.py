class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        def landFollowing(grid, i, j):
            
            if(grid[i][j]=='0'):
                return 
            else:
                grid[i][j]='0'
                

            if(i-1>=0):
                if(grid[i-1][j]=='1'):
                    landFollowing(grid, i-1,j);
                    
            if(i+1<=len(grid)-1):
                if( grid[i+1][j]=='1'):
                    landFollowing(grid, i+1,j);
                    
            if(j-1>=0):
                if(grid[i][j-1]=='1'):
                    landFollowing(grid, i,j-1);
                
            if(j+1<=len(grid[i])-1):
                if( grid[i][j+1]=='1'):
                    landFollowing(grid, i,j+1);
            
                
                    
                    
        
        
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if(grid[m][n])=='1':
                    count+=1
                    landFollowing(grid, m,n)
        return count
            
        