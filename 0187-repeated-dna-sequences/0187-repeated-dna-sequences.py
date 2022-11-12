class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        sequenceCount = {}
        
        left = 0
        while left+10<=len(s):
            part = s[left:left+10]
            if part in sequenceCount:
                sequenceCount[part]+=1
            else:
                sequenceCount[part]=1
            left+=1
        
        res = []
        for k,v in sequenceCount.items():
            if v>1:
                res.append(k)
        
        return res