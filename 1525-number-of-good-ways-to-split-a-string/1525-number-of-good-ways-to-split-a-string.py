class Solution:
    def numSplits(self, s: str) -> int:
        
        m = len(s)
        count = 0
                
        distincLeft = [1 for i in range(m)]
        distincRight = [1 for i in range(m)]
        
        leftSet = set()
        leftSet.add(s[0])
        for i in range(1, len(s)):
            l = s[i]
            if l not in leftSet:
                distincLeft[i] = distincLeft[i-1]+1
            else:
                distincLeft[i] = distincLeft[i-1]
            leftSet.add(l)
                    
        currRightMap = {}
        for i in range(len(s)-1,-1,-1):
            l = s[i]
            if l not in currRightMap:
                if i<len(s)-1:
                    distincRight[i] = distincRight[i+1]+1
                else:
                    distincRight[i] = 1
                currRightMap[l] = 1
            else:
                if i<len(s)-1:
                    distincRight[i] = distincRight[i+1]
                else:
                    distincRight[i] = 1
        
        for i in range(len(s)-1):
            if distincLeft[i]==distincRight[i+1]:
                count+=1
        
        return count
            
        