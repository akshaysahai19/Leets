class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def findPair(listVal, pair):
            
            if len(listVal)==0:
                result.append(pair)
                return
            
            for i in range(len(listVal)):
                findPair(listVal[:i]+listVal[i+1:], pair+[listVal[i]])
        
        findPair(nums, [])
        
        return result
            