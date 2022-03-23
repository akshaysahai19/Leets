class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        lettersMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        combinationsMap = {}
        
        for i in lettersMap.keys():
            for j in lettersMap.keys():
                digitsWord = i+j
                word1_len = len(lettersMap[i])
                word2_len = len(lettersMap[j])
                for k in range(word1_len):
                    for l in range(word2_len):
                        letter1 = lettersMap[i][k]
                        letter2 = lettersMap[j][l]
                        if digitsWord not in combinationsMap:
                            combinationsMap[digitsWord] = [''+letter1+letter2]
                        else:
                            combinationsMap[digitsWord].append(''+letter1+letter2)
        
        
        
        output = []
        
        if len(digits)==1:
            for letters in lettersMap[digits[0]]:
                output.append(letters)
        
        if len(digits)==2:
            return combinationsMap[digits[0]+digits[1]]
        
        if len(digits)==3:
            for letters in lettersMap[digits[0]]:
                for items in combinationsMap[digits[1]+digits[2]]:
                    output.append(letters+items)
        
        if len(digits)==4:
            for firstTwo in combinationsMap[digits[0]+digits[1]]:
                for lastTwo in combinationsMap[digits[2]+digits[3]]:
                    output.append(firstTwo+lastTwo)
        
        print(output)
        return output
                    