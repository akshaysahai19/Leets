class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        currentMax = 0
        for i in range(len(nums)):
            currentMax = max(currentMax, i+nums[i])
            if currentMax>=len(nums)-1:
                return True
            if nums[i]==0 and currentMax==i:
                return False
        return False
            
        