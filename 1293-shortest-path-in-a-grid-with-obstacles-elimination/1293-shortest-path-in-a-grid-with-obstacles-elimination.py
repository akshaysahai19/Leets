class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        paths = []
        
        seen = set()
        
        queue = [[0, 0, 0, 0]]
        
        ans = float('inf')
        
        while queue:
            count, removed, r,c= heapq.heappop(queue)
            
            if r==m-1 and c==n-1:
                return count
            
            for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                
                if x>=0 and x<m and y>=0 and y<n and (x,y, removed+grid[x][y]) not in seen:
                    
                    if grid[x][y]==1:
                        rCount = removed+1
                        if rCount<=k:
                            heapq.heappush(queue, [count+1, rCount, x, y])
                            seen.add((x,y, rCount))
                    else:
                        heapq.heappush(queue, [count+1, removed, x, y])
                        seen.add((x,y, removed))

        
        return -1
    
        
            