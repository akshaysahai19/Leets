class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def findWord(i,j, w):
            if not w:
                return True
            
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=w[0]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            a = findWord(i+1,j,w[1:])
            b = findWord(i-1,j,w[1:])
            c = findWord(i,j+1,w[1:])
            d = findWord(i,j-1,w[1:])
            board[i][j] = temp
            if a or b or c or d:
                return True
            return False
        
        for i in range(m):
            for j in range(n):
                if findWord(i,j, word):
                    return True
                    
        
        return False
            
        
        
        