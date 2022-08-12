class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordStorage = {}
        
        def isPossible(newS):
            
            if len(newS) in wordStorage:
                return wordStorage[len(newS)]
            
            if len(newS)==0:
                return True
            
            for word in wordDict:
                if newS[:len(word)]==word:
                    newLen = len(newS[len(word):])
                    wordStorage[newLen] = isPossible(newS[len(word):])
                    if wordStorage[newLen]:
                        return True
            
            return False
            
            
        return isPossible(s)
        