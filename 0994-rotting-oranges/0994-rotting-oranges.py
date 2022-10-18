class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def rot(x, y, time, state):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==0 or (grid[x][y]<0 and -grid[x][y]<time):
                return 
            
            if state==0 and grid[x][y]==2:
                return 
            
            grid[x][y] = -time
            rot(x+1,y, time+1, 0)
            rot(x-1,y, time+1, 0)
            rot(x,y+1, time+1, 0)
            rot(x,y-1, time+1, 0)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rot(i,j,0, 1)
        
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
                print(abs(grid[i][j]))
                time = max(abs(grid[i][j]), time)
        print(grid)
        return time
        