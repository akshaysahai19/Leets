class Solution:
    def romanToInt(self, romans: str) -> int:
        finalInt = 0
        def findInt(num):
            if num[:2]=='CM':
                return 900, 2
            elif num[:2]=='CD':
                return 400, 2
            elif num[:2]=='XC':
                return 90, 2
            elif num[:2]=='XL':
                return 40, 2
            elif num[:2]=='IX':
                return 9, 2
            elif num[:2]=='IV':
                return 4, 2
            elif num[0]=='M':
                return 1000, 1
            elif num[0]=='D':
                return 500, 1
            elif num[0]=='C':
                return 100, 1
            elif num[0]=='L':
                return 50, 1
            elif num[0]=='X':
                return 10, 1
            elif num[0]=='V':
                return 5, 1
            elif num[0]=='I':
                return 1, 1
            
        val = romans
        while len(val)>0:
            intResult, updateWith = findInt(val)
            val = val[updateWith:]
            finalInt+=intResult

        return finalInt   
                
        
                