class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        m = len(tops)
        topChanges = 0
        topReverseChanges = 1
        changedTop = [tops[0]]
        reverseTop = [bottoms[0]]
        for i in range(1, m):
            if changedTop[-1]!=tops[i] and changedTop[-1]==bottoms[i]:
                topChanges+=1
                changedTop.append(bottoms[i])
            elif changedTop[-1]==tops[i]:
                changedTop.append(tops[i])
                
            
            if reverseTop[-1]!=tops[i] and reverseTop[-1]==bottoms[i]:
                topReverseChanges+=1
                reverseTop.append(bottoms[i])
            elif reverseTop[-1]==tops[i]:
                reverseTop.append(tops[i])

        bottomChanges = 0
        bottomReverseChanges = 1
        reverseBottom = [tops[0]]
        changedBottom = [bottoms[0]]
        for i in range(1, m):
            if changedBottom[-1]!=bottoms[i] and changedBottom[-1]==tops[i]:
                bottomChanges+=1
                changedBottom.append(tops[i])
            elif changedBottom[-1]==bottoms[i]:
                changedBottom.append(bottoms[i])
            
            if reverseBottom[-1]!=bottoms[i] and reverseBottom[-1]==tops[i]:
                bottomReverseChanges+=1
                reverseBottom.append(tops[i])
            elif reverseBottom[-1]==bottoms[i]:
                reverseBottom.append(bottoms[i])
                    
        ans = float('inf')
        
        if len(changedTop)==m:
            ans = min(ans, topChanges)
        
        if len(reverseTop)==m:
            ans = min(ans, topReverseChanges)
            
        if len(changedBottom)==m:
            ans = min(ans, bottomChanges)
        
        if len(reverseBottom)==m:
            ans = min(ans, bottomReverseChanges)
        
        if ans!=float('inf'):
            return ans
        return -1
        
        