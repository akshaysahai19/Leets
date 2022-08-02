class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        def backTrack(board, word, i, j):
            
            
            if not word:
                return True
            
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
                return False
            
            
            temp = board[i][j]
            board[i][j] = '#'
            if backTrack(board,word[1:],i+1, j) or backTrack(board,word[1:],i-1, j) or backTrack(board,word[1:],i, j-1) or backTrack(board,word[1:],i, j+1):
                return True
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backTrack(board, word, i, j):
                    return True
        return False
        