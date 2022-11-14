class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        pairs = []
        m = len(s)
        
        if m==4:
            val = '.'.join(list(s))
            return [val]
        if m<4:
            return []
        
        def backtrack(curr, index, pair):
            
            if not curr or (len(curr)>1 and curr[0]=='0'):
                return
            
            if int(curr)<0 or int(curr)>255:
                return
            
            if index==m:
                if len(pair+[curr])==4 and ''.join(pair+[curr])==s:
                    pairs.append('.'.join(pair+[curr]))
                    return
                return
            
            
            if int(curr)>=0 and int(curr)<=255:
                backtrack(curr+s[index], index+1, pair)
            
            backtrack(s[index], index+1, pair+[curr])
                
        backtrack(s[0], 1, [])
        
        return pairs
            
            
        