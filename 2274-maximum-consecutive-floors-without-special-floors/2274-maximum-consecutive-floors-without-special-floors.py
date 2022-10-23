class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
#         specials = {}
#         for s in special:
#             specials[s]=1
            
#         currMax = 0
#         curr = 0
#         for i in range(bottom, top+1):
#             if i in specials:
#                 currMax = max(currMax, curr)
#                 curr = 0
#             else:
#                 curr+=1
#         currMax = max(currMax, curr)        
#         return currMax

        special.sort()
        answer = 0
        answer = max(answer, special[0]-bottom, top-special[len(special)-1])
        for i in range(1, len(special)):
            answer = max(answer, special[i]-special[i-1]-1)
        return answer
            
            
            
            
        