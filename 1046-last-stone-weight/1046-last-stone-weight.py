class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        while len(stones)>0:
            if len(stones)==1:
                return stones[0]
            
            end = len(stones)-1
            stones.sort()
            if stones[end]!=stones[end-1]:
                diff = stones[end]-stones[end-1]
                stones.pop()
                stones[end-1]=diff
            else:
                stones.pop()
                stones.pop()
            
            
        return 0
    
        