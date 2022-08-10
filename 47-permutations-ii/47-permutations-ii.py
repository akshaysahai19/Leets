class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def findPerms(listNum, pair):
            if not listNum:
                if pair not in result:
                    result.append(pair)
                return
            
            for i in range(len(listNum)):
                findPerms(listNum[:i]+listNum[i+1:], pair+[listNum[i]])
            
        findPerms(nums, [])
        
        return result
        
        