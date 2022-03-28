class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        originalNum = []
        
        for vals in nums:
            originalNum.append(vals)
            
        mapping = {}
        nums.sort()
        
        for i,val in enumerate(nums):
            if val not in mapping:
                mapping[val]=i
        
        result = []
        
        for val in originalNum:
            result.append(mapping[val])
            
        return result
            
            
        