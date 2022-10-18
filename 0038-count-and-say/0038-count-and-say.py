class Solution:
    def countAndSay(self, n: int) -> str:
        
        def findSay(localN, itr):
            if itr==n:
                return localN
            
            val = ''
            count = 0
            for i in range(len(localN)):
                if i!=len(localN)-1:
                    if localN[i]==localN[i+1]:
                        count+=1
                    else:
                        temp = str(count+1)
                        val+=(temp+localN[i])
                        count=0
                else:
                    temp = str(count+1)
                    val+=(temp+localN[i])
            
            return findSay(val, itr+1)
        
        return findSay("1", 1) 
                    
                