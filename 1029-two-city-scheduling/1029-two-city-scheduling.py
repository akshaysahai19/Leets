class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x:x[0]-x[1])
        
        totalCosts = 0
        parts = len(costs)//2
        for i in range(parts):
            totalCosts+=(costs[i][0]+costs[i+parts][1])
        return totalCosts
                
            
        