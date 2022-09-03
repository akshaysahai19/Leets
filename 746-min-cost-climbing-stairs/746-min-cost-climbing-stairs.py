class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mem = {}
        
        def findMinCost(i):
            
            if i in mem:
                return mem[i]
            
            if i>=len(cost):
                return 0
            # if i==len(cost)-1:
            #     return cost[i]
            mem[i] = cost[i] + min(findMinCost(i+1), findMinCost(i+2))
            return mem[i]
        
        return min(findMinCost(0),findMinCost(1))
            