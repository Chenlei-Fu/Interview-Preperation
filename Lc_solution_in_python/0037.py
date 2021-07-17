from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        DFS + backtracking
        """
        self.doSolve(board)

    def doSolve(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.': continue
                for tmp in range(ord('1'), ord('9') + 1):
                    chr_tmp = chr(tmp)
                    if self.isValid(chr_tmp, board, i, j):
                        board[i][j] = chr_tmp
                        if self.doSolve(board):
                            return True
                        else:
                            board[i][j] = '.'  # backtracking
                return False  # all trials are invalid
        return True

    def isValid(self, tmp, board, row, col):
        for i in range(9):
            if board[i][col] == tmp: return False
            if board[row][i] == tmp: return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == tmp: return False
        return True