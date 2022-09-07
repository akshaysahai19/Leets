class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        dp = {}
        
        def maxRob(start, end):
            
            if (start, end) in dp:
                return dp[(start, end)]
            
            if end>len(nums)-1:
                return 0
            
            if end==len(nums)-1:
                if start==0:
                    return 0
            
            dp[(start, end)] = nums[end] + max(maxRob(start, end+2), maxRob(start, end+3))
            return dp[(start, end)]
        
        maxAmount = 0
        for i in range(len(nums)):
            maxAmount = max(maxAmount, maxRob(i,i))
        
        return maxAmount
        