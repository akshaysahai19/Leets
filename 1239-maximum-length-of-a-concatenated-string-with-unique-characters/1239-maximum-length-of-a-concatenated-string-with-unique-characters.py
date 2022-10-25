class Solution:
    
    def maxLength(self, arr: List[str]) -> int:
        
        pairs = []
        # @ naman
        def checkPair(curr, index):
            if len(curr)!=len(set(curr)):
                return
            
            # pairs.append(curr)
            pairs.append(len(curr))
            for i in range(index+1, len(arr)):
                checkPair(curr+arr[i], i)
            
            return curr
    
        checkPair('', -1)

#         res = 0
#         for pair in pairs:
#             res = max(res, len(pair))
        
#         return res
        return max(pairs)
            
            
            