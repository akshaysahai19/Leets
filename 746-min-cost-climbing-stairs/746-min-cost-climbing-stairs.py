class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem = {}
        
        def getMinCost(n):
            if n in mem:
                return mem[n]
            
            if n>len(cost)-1:
                return 0
            
            mem[n] = cost[n]+min(getMinCost(n+1), getMinCost(n+2))
            return mem[n]
        
        return min(getMinCost(1), getMinCost(0))