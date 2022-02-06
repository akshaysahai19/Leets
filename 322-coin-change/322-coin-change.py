class Solution(object):
    
    
    def minCoinChange(self, coins, amount, mem):
        
        if(amount==0):
            return 0
        
        if(amount<0):
            return -1
        
        if(amount not in mem):
            mem[amount] = 1 + min(self.minCoinChange(coins, amount-coins[i], mem) if coins[i]<=amount else float('inf') for i in range(len(coins)))       
        return mem[amount]
    
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem = {}
        if(self.minCoinChange(coins,amount, mem)==float('inf')):
            return -1
        else:
            return self.minCoinChange(coins,amount, mem)
        