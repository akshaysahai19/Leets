class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        
        def maxAmount(n):
            
            if n in dp:
                return dp[n]
            
            if n>=len(nums):
                return 0
            
            dp[n] = nums[n] + max(maxAmount(n+2), maxAmount(n+3))
            return dp[n]
        
            # return nums[n]
        
        return max(maxAmount(0), maxAmount(1))
    
    
    