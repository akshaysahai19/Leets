import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        diffs = []
        
        curr = heights[0]
        for i in range(1, len(heights)):
            diff = curr-heights[i]
            curr = heights[i]
            if diff<0:
                bricks+=diff
                heapq.heappush(diffs, diff)
                if bricks<0:
                    ladders-=1
                    bricks-=heapq.heappop(diffs)
                
                    if bricks<0 or ladders<0:
                        return i-1
                    
                                        
        return n-1