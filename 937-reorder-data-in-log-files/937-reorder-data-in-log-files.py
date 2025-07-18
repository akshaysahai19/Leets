class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    
        numbers = ['0','1','2','3','4','5','6','7','8','9']
    
        digitLogs = []
        wordLogs = []
        
        for log in logs:
            logArray = log.split(' ')
            if logArray[1][0] in numbers:
                digitLogs.append(log)
            else:
                wordLogs.append(logArray)
        
        wordLogs = sorted(wordLogs, key=lambda x:(x[1:], x[0]))
        
        result = []
        for log in wordLogs:
             result.append(' '.join(log))
        result+=digitLogs
        
        return result
            
        
        