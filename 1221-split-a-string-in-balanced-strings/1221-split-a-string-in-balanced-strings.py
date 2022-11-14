class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        left = 0
        right = 1
        pair = []
        
        curr = ''
        currR = 0
        currL = 0
        while left<len(s):
            if s[left]=='R':
                currR+=1
            elif s[left]=='L':
                currL+=1
            curr+=s[left]
            
            if currR==currL:
                pair.append(curr)
                curr = ''
                currR = 0
                currL = 0
            left+=1
        print(pair)
        return len(pair)
                
        