class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def findRes(arr):
            
            if len(arr)==1:
                return arr[0]
            
            curr = []
            for i in range(0, len(arr)-1):
                val = (arr[i]+arr[i+1])%10
                curr.append(val)
            return findRes(curr)
        
        ans = findRes(nums)
        
        return ans
        