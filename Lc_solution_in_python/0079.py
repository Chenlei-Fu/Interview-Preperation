from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS -> test all the entries
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (self.dfs(board, i, j, 0, word)): return True
        return False

    def dfs(self, board, x, y, i, word):
        if i == len(word): return True
        if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or board[x][y] != word[i]: return False
        tmp = board[x][y]
        board[x][y] = '#'  # mark as visited
        # try all directions
        exist = self.dfs(board, x + 1, y, i + 1, word) or self.dfs(board, x - 1, y, i + 1, word) or self.dfs(board, x,
                                                                                                             y + 1,
                                                                                                             i + 1,
                                                                                                             word) or self.dfs(
            board, x, y - 1, i + 1, word)
        board[x][y] = tmp
        return exist