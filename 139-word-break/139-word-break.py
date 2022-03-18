class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def checkWordBreak(newS, index, memo):
            
            if index in memo:
                return memo[index]
            
            if len(newS)==0:
                return True
            
            for x in wordDict:
                if len(newS)>=len(x):
                    # print(newS[:len(x)])
                    if x == newS[:len(x)]:
                        i = len(s)-len(newS[len(x):])
                        result = checkWordBreak(newS[len(x):], i, memo)
                        memo[i] = result
                        if result:
                            return True
                
            return False
        
        return checkWordBreak(s, 0, {})