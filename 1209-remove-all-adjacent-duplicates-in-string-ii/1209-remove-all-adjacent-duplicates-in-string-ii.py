class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = [[s[0],1]]
        
        for i in range(1, len(s)):
            if stack:
                if stack[-1][0]==s[i]:
                    stack[-1][1]+=1
                    if stack[-1][1]==k:
                        stack.pop()
                else:
                    stack.append([s[i],1])
            else:
                stack.append([s[i],1])
                
        res = ''
        for i in range(len(stack)):
            res+=(stack[i][0]*stack[i][1])
        print(stack)
        return res
        