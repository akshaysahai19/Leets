class Solution:
    def decodeString(self, s: str) -> str:

        ans = ''
        stack = []
        for c in s:
            if c==']':
                curr = ''
                num = ''
                while stack and stack[-1]!='[':
                    curr = stack.pop()+curr
                if stack[-1]=='[':
                    stack.pop()
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                if num!='':
                    curr*=int(num)
                stack.append(curr)
            else:
                stack.append(c)

        while stack:
            ans+=stack.pop(0)

        return ans


                    