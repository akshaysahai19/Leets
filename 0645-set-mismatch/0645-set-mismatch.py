class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        missing = 0
        present = {}
        
        for n in nums:
            if n in present:
                present[n]+=1
            else:
                present[n]=1
        
        for i in range(0, len(nums)):
            if i+1 in present:
                if present[i+1]==2:
                    duplicate = i+1
            else:
                missing = i+1
        
        return [duplicate, missing]
        