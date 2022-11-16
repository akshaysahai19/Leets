class Solution:
    def numSplits(self, s: str) -> int:
        
        m = len(s)
        count = 0
                
        distincLeft = [0 for i in range(m)]
        distincRight = [0 for i in range(m)]
        
        currLeftMap = {}
        for i, l in enumerate(s):
            if l not in currLeftMap:
                if i>0:
                    distincLeft[i] = distincLeft[i-1]+1
                else:
                    distincLeft[i] = 1
                currLeftMap[l] = 1
            else:
                if i>0:
                    distincLeft[i] = distincLeft[i-1]
                else:
                    distincLeft[i] = 1
                    
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
            
        