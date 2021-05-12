class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        brute fource
        """
        
        while True:
            # check
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if i > 1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                        crush |= {(i, j), (i-1,j), (i-2, j)} # update
                    if j > 1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                        crush |= {(i, j), (i,j-1), (i, j-2)} # update

            if not crush: 
                break
            for i, j in crush:
                board[i][j] = 0
            
            # drop: 283 move zeros in each column
            for j in range(len(board[0])):
                cur = len(board) - 1
                for i in reversed(range(len(board))):
                    if board[i][j]:
                        board[cur][j] = board[i][j]
                        cur -= 1
                for k in range(cur+1):
                    board[k][j] = 0
        return board
    
        
            
            
            