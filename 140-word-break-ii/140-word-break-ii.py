class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        pairs = []
        
        def findPairs(newS, sentence):
            if len(newS)==0:
                pairs.append(sentence[1:])
                return sentence
            
            for word in wordDict:
                if len(newS)>=len(word):
                    if word==newS[:len(word)]:
                        pair = findPairs(newS[len(word):], sentence+" "+word)
                        # print(pair)
                        # pairs.append(pair)
            
            return ''
        
        
        findPairs(s, '')
        
        return pairs