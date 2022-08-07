class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        pairs = []
        
        def printPermutations(index, pair):
            if index==len(s):
                pairs.append(pair)
                return pair
            
            char = s[index]
            originalPair = pair
            originalPair+=char
            printPermutations(index+1, originalPair)
            if not char.isdigit():
                if char.isupper():
                    pair+=char.lower()
                    printPermutations(index+1, pair)
                else:
                    pair+=char.upper()
                    originalPair+=char
                    printPermutations(index+1, pair)
            
            return pairs
            
        if not s:
            return []
        
        return printPermutations(0, "")