class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n = len(heights)
        m = len(heights[0])
        seen = set()
        seen.add((0,0))
        queue = [[heights[0][0],0, 0]]
        ans = 0
        
        while queue:
            
            h,r,c = heapq.heappop(queue)
            if r!=0 or c!=0:
                ans = max(ans, h)
                
            seen.add((r,c))
            
            if r==n-1 and c==m-1:
                return ans
            
            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if x>=0 and x<n and y>=0 and y<m and (x,y) not in seen:
                    print('yes')
                    heapq.heappush(queue, [abs(heights[x][y]-heights[r][c]), x, y])
                    
        