class TicTacToe:
    
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        curPlayer = 1 if player == 1 else -1
        # actions on row and col
        self.row[row] += curPlayer
        self.col[col] += curPlayer
        
        # actions on diagonal / anti_diagonal
        self.diagonal += curPlayer if row == col else 0
        self.anti_diagonal += curPlayer if row + col == self.n-1 else 0 # important! it's not equal to `self.n`
        
        # check winner
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)