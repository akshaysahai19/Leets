class Solution:
    
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        data = []
    
        def countCombinationSum(candidates, target, pairs, start):
            if target==0:
                if list(pairs) not in data:
                    data.append(list(pairs))
                return


            if target<0:
                return

            for i in range(start, len(candidates)):
                pairs.append(candidates[i])
                countCombinationSum(candidates, target-candidates[i], pairs, i)
                pairs.pop()

        
        countCombinationSum(candidates, target, [], 0)
            
        return data  