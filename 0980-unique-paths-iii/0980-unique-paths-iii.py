class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        
        start_row, start_col = 0, 0
        end_row, end_col = m-1, n-1
        non_obstacle_points = 0
        for row in range(0, m):
            for col in range(0, n):
                cell = grid[row][col] 
                if cell == 1:
                    start_row, start_col = row, col
                if cell == 2:
                    end_row, end_col = row, col
                if cell !=-1:
                    non_obstacle_points+=1
                
        paths = []
        total = 0
        print('start = ', start_row, start_col)
        print('end = ', end_row, end_col)
        def countPaths(x, y, curr, rem):
            nonlocal total
            
            if x<0 or y<0 or x>=m or y>=n or grid[x][y]<0:
                return
            
            if x==end_row and y==end_col and rem==1:
                total+=1
                paths.append(curr)
                print('path = ', curr)
                return
            
            temp = grid[x][y]
            grid[x][y]=-2
            
            countPaths(x,y+1, curr+[(x,y)], rem-1)
            countPaths(x+1,y, curr+[(x,y)], rem-1)
            countPaths(x-1,y, curr+[(x,y)], rem-1)
            countPaths(x,y-1, curr+[(x,y)], rem-1)
            
            grid[x][y] = temp
        
        countPaths(start_row,start_col, [], non_obstacle_points)
        print(paths)
        return total
        