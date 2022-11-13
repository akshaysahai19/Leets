class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        words = []
        
        for w in s.split(' '):
            if w.strip()!='':
                words.append(w.strip())
        
        ans = ''
        
        right = len(words)-1
        while right>=0:
            ans=ans+' '+words[right]
            right-=1
        return ans.strip()
            