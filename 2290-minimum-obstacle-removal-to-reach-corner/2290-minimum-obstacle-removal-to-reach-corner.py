class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        paths = []
        
        seen = set()
        seen.add((0,0))
        
        queue = [[0, 0, 0]]
        
        while queue:
            removed, r, c = heapq.heappop(queue)
            
            if r==m-1 and c==n-1:
                return removed
                
            for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                
                if x>=0 and x<m and y>=0 and y<n and (x,y) not in seen:
                    
                    heapq.heappush(queue, [removed+grid[x][y], x, y])
                    seen.add((x,y))

        
        return -1