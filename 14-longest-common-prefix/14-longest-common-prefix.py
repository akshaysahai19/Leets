class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==1):
            return strs[0]
        x = 0
        prefix_map = {}
        # strs = strs.sort()
        while x<len(strs[0]):
            for word in strs:
                val = strs[0][0:x+1]
                if val in word[:len(val)]:
                    if val in prefix_map: 
                        prefix_map[val]+=1
                    else:
                        prefix_map[val]=1
            x+=1
        maxPrefix = ''
        for k,v in prefix_map.items():
            if v==len(strs) and len(k)>len(maxPrefix):
                maxPrefix = k    
        return maxPrefix