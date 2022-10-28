class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)-1
        seen = [(0,0)]
        queue = [(grid[0][0], 0, 0)]
        ans = 0
        while queue:
            d,r,c = heapq.heappop(queue)
            ans = max(ans, d)
            
            if r==c==n:
                return ans
            
            if c>=0 and c<=n:
                if r-1>=0 and (r-1, c) not in seen:
                    heapq.heappush(queue, (grid[r-1][c], r-1, c))
                    seen.append((r-1, c))
                    
                if r+1<=n and (r+1, c) not in seen:
                    heapq.heappush(queue, (grid[r+1][c], r+1, c))
                    seen.append((r+1, c))
            
            if r>=0 and r<=n:
                if c-1>=0 and (r, c-1) not in seen:
                    heapq.heappush(queue, (grid[r][c-1], r, c-1))
                    seen.append((r-1, c))
                    
                if c+1<=n and (r, c+1) not in seen:
                    heapq.heappush(queue, (grid[r][c+1], r, c+1))
                    seen.append((r, c+1))
        
        