class Solution:
    def rob(self, nums: List[int]) -> int:
        
#         dp = {}
        
#         def maxAmount(n):
            
#             if n in dp:
#                 return dp[n]
            
#             if n>=len(nums):
#                 return 0
            
#             for i in range(n+2, len(nums)):
#                 dp[n] = nums[n] + max(maxAmount(i), maxAmount(i+1))
#                 return dp[n]
        
#             return nums[n]
        
#         return max(maxAmount(0), maxAmount(1))

        dp = [0]*(len(nums))
        dp[0] = nums[0]
        if len(dp)>1:
            dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return max(dp)
    
    
    