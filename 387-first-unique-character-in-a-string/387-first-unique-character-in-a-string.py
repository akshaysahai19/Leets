class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        countIndexMap = {}
        for i, letter in enumerate(s):
            if letter in countIndexMap:
                countIndexMap[letter][1] = countIndexMap[letter][1]+1
            else:
                countIndexMap[letter] = [i,0]
        
        for k,v in countIndexMap.items():
            if v[1]==0:
                return v[0]
        
        return -1
                
            