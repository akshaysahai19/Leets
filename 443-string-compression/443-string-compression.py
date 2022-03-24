class Solution:
    def compress(self, chars: List[str]) -> int:
        var = ''
        count = 0
        for i in range(len(chars)):
            if i!=len(chars)-1:
                if chars[i]==chars[i+1]:
                    count+=1
                else:
                    if count==0:
                        var=var+chars[i]
                    else:
                        var=var+chars[i]+str(count+1)
                    count=0
            else:
                if count==0:
                    var=var+chars[i]
                else:
                    var=var+chars[i]+str(count+1)
        
        for i in range(len(var)):
            chars[i]=var[i]
            
        return len(var)
            
                
                        
        