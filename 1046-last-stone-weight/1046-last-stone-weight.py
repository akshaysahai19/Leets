class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def minStone(leftStones: List[int]):
            if len(leftStones)==1:
                return leftStones[0]
            elif len(leftStones)==0:
                return 0
            
            end = len(leftStones)-1
            if leftStones[end]>leftStones[end-1]:
                diff = leftStones[end]-leftStones[end-1]
                leftStones=leftStones[:end-1]
                leftStones.append(diff)
                leftStones.sort()
                return minStone(leftStones) 
            else:
                leftStones=leftStones[:end-1]
                return minStone(leftStones) 
                
            
        stones.sort()
        print(stones)
        return minStone(stones)
    
        