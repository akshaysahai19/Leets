class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        
        def borderFlag(i,j):
            
            if i>=m or i<0 or j>=n or j<0 or board[i][j]!='O':
                return
            
            board[i][j]='B'
            a = borderFlag(i+1,j)
            b = borderFlag(i-1,j)
            c = borderFlag(i,j+1)
            d = borderFlag(i,j-1)
            

        for i in range(m):
            for j in range(n):
                if (i==0 or j==0 or i==m-1 or j==n-1) and board[i][j]=='O':
                    borderFlag(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='B':
                    board[i][j] = 'O'
        

