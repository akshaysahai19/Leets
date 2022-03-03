class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """   
        return min(self.minCost(cost,0,{}), self.minCost(cost, 1, {}))
    
    def minCost(self, cost, i, mem):
        if i in mem:
            return mem[i]
        
        if i>len(cost)-1:
            return 0
            
        mem[i] = cost[i]+min(self.minCost(cost,i+1,mem), self.minCost(cost,i+2,mem))
        return mem[i] 
        