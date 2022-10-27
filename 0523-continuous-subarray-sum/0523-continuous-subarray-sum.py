class Solution:
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mem = {0:0}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            
            if total%k not in mem:
                mem[total%k] = i+1
            elif mem[total%k]<i:
                    return True
        return False
        
        
        