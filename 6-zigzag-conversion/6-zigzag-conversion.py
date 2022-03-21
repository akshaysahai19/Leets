class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = 0
        index = 0
        isUp = False
        zigzagMap = {}
        
        if numRows == 1:
            return s
        
        while rows<numRows and index<len(s):
            
            if rows in zigzagMap:
                zigzagMap[rows].append(s[index])
            else:
                zigzagMap[rows] = [s[index]]
            
            if isUp:
                if rows==0:
                    isUp =False
                    rows+=1
                else:
                    rows-=1
            else:
                if rows==numRows-1:
                    isUp = True
                    rows-=1
                else:
                    rows+=1
            index+=1
        
        
        
        finalOutput = ''
        for i in range(len(zigzagMap)):
            for j in range(len(zigzagMap[i])):
                finalOutput+=zigzagMap[i][j]    
                
        print(zigzagMap)
        print(finalOutput)
        return finalOutput
                
                
            
            
        