class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        posMap = {}
        posMap['-'] = 99
        for i,val in enumerate(order):
            posMap[val]=i
        
        maxLen = 0
        for word in words:
            maxLen = max(maxLen, len(word))
        for i in range(len(words)):
            if len(words[i])<maxLen:
                words[i]+=(maxLen-len(words[i]))*'-'
        
        for i in range(len(words)-1):
            for j in range(maxLen):
                letter1 = words[i][j]
                letter2 = words[i+1][j]
                if letter1!=letter2:
                    if letter1!='-' and letter2=='-':
                        return False
                    if letter1!='-':
                        if posMap[letter1]>posMap[letter2]:
                            return False
                        break
                
        return True
                        