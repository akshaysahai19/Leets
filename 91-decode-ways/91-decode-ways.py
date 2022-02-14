class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}
        
        def countNumDecodings(index, check):
            # print('index = ',index,' check = ',check)
            if (index,check) in dp:
                return dp[(index,check)]
            
            if check==1:
                if index==len(s)-1:
                    if s[index]=='0':
                        return 0
                elif s[index]=='0':
                        return 0
            elif check==2:
                if index==len(s)-1:
                    if s[index-1]=='0' or int(s[index-1]+s[index])>26:
                        return 0
                elif s[index-1]=='0' or int(s[index-1]+s[index])>26:
                    return 0
                    
            # elif(check==2):
            if index+2<=len(s)-1:
                dp[(index,check)] = countNumDecodings(index+1,1) + countNumDecodings(index+2,2) 
            elif index+1<=len(s)-1:
                dp[(index,check)] = countNumDecodings(index+1,1)
            else:
                dp[(index,check)] = 1
            # print('Hello = ',s[index:])
            return dp[(index,check)]
            
        
        return countNumDecodings(-1,3)
                    