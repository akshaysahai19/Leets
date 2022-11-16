class Solution:
    def numSplits(self, s: str) -> int:
        
        m = len(s)
        count = 0
                
        distincLeft = [1 for i in range(m)]
        distincRight = [1 for i in range(m)]
        
        leftSet = set(s[0])
        for i in range(1, len(s)):
            l = s[i]
            if l not in leftSet:
                distincLeft[i] = distincLeft[i-1]+1
            else:
                distincLeft[i] = distincLeft[i-1]
            leftSet.add(l)
                    
        rightSet = set(s[m-1])
        for i in range(len(s)-2,-1,-1):
            l = s[i]
            if l not in rightSet:
                distincRight[i] = distincRight[i+1]+1
                rightSet.add(l)
            else:
                distincRight[i] = distincRight[i+1]
            
        
        for i in range(len(s)-1):
            if distincLeft[i]==distincRight[i+1]:
                count+=1
        
        return count
            
        