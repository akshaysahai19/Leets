class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def isMatchedWord(m, n, word):
            
            if not word:
                return True
            
            if m<0 or m>=len(board) or n<0 or n>=len(board[0]) or board[m][n]!=word[0]:
                return False
            
            temp = ""
            if board[m][n]==word[0]:
                temp = word[0]
                board[m][n]="#"
            
            if (isMatchedWord(m+1,n, word[1:]) or isMatchedWord(m-1,n, word[1:]) or isMatchedWord(m,n-1, word[1:]) or isMatchedWord(m,n+1, word[1:])):
                return True
            
            if temp!="":
                board[m][n] = temp
            return False
        
        def findWord():
            for m in range(len(board)):
                for n in range(len(board[0])):
                    if isMatchedWord(m,n, word):
                        return True
            
            return False
        
        return findWord()
        