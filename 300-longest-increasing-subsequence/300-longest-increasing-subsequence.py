class Solution:
    
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for end in range(len(nums)):
            for start in range(0, end):
                if nums[end]>nums[start]:
                    dp[end]=max(dp[end],1+dp[start])
                    
        return max(dp)