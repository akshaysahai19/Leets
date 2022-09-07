class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        
        def maxAmount(n):
            
            if n in dp:
                return dp[n]
            
            if n>=len(nums):
                return 0
            
            for i in range(n+1, len(nums)):
                dp[n] = nums[n] + max(maxAmount(i+1), maxAmount(i+2))
                return dp[n]
        
            return nums[n]
        
        return max(maxAmount(0), maxAmount(1))
    
    
    